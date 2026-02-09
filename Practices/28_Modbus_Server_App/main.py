from pymodbus.server.sync import StartUdpServer, StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSequentialDataBlock
import logging
import threading
import time
import multiprocessing
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPainter, QPen
from PyQt5.QtCore import *
import json
import qdarkstyle
from pathlib import Path

class MyModbusServer:
    def __init__(self, ip_address, port, num_registers):
        self.ip_address = ip_address
        self.port = port
        self._lock = threading.Lock()

        ir_dict = dict({
            **{i: 0 for i in range(1, num_registers)},

            # 49999 ~ 50099
            **{i: 0 for i in range(49999, 50100)},})

        # Input register blocks
        ir_block = ModbusSparseDataBlock(ir_dict)

        self.context = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0] * num_registers),
            co=ModbusSequentialDataBlock(0, [0] * num_registers),
            hr=ModbusSequentialDataBlock(0, [0] * num_registers),
            ir=ir_block,
        )


        self.device = ModbusServerContext(slaves=self.context, single=True)

        self.context.setValues(4, 0, [3] * 1000)

        print(f"Starting exp master server on port {port} with {num_registers} registers")

        self.server_thread = threading.Thread(target=self.start_server, daemon=True).start()


    def start_server(self):
        StartUdpServer(self.device, address=(self.ip_address, self.port))

    def set_holding_registers(self, address, values):
        with self._lock:
            self.context.setValues(3, address, values)

    def set_input_registers(self, address, values):
        with self._lock:
            self.context.setValues(4, address, values)


class MyMainWindow(QWidget):
    def __init__(self, ip_address, port, num_registers, start_address = 0):
        super().__init__()
        self.start_address = start_address
        self.server = MyModbusServer(ip_address, port, num_registers)
        self.setWindowTitle("PyQt Modbus Server")

        # Set global font size
        font = QFont()
        font.setPointSize(15)
        self.setFont(font)

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # --- Create Tab Control ---
        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        # --- Tab 1 ---
        tab1 = QWidget()
        tabs.addTab(tab1, "Holding Registers")
        tab1_layout = QVBoxLayout(tab1)

        # Scroll area 1
        scroll1 = QScrollArea()
        scroll1.setWidgetResizable(True)
        tab1_layout.addWidget(scroll1)

        # ----------------------
        # Scroll content widget
        # ----------------------
        content1 = QWidget()
        scroll1.setWidget(content1)

        grid1 = QGridLayout(content1)
        grid1.setSpacing(0)

        for j in range(100):
            for i in range(10):
                grid1.addWidget(MyCell(self.start_address + j * 10 + i, self.server, True), i, j)

        # --- Tab 2 ---
        tab2 = QWidget()
        tabs.addTab(tab2, "Input Registers")
        tab2_layout = QVBoxLayout(tab2)

        # Scroll area 2
        scroll2 = QScrollArea()
        scroll2.setWidgetResizable(True)
        tab2_layout.addWidget(scroll2)

        # ----------------------
        # Scroll content widget
        # ----------------------
        content2 = QWidget()
        scroll2.setWidget(content2)

        grid2 = QGridLayout(content2)
        grid2.setSpacing(0)

        for j in range(100):
            for i in range(10):
                grid2.addWidget(MyCell(self.start_address + j * 10 + i, self.server, False), i, j)

        # --- Tab 3 ---
        tab3 = QWidget()
        tabs.addTab(tab3, "Tab 3")

        grid3 = QGridLayout()
        tab3.setLayout(grid3)

        grid3.addWidget(QPushButton("T3 First"), 0, 0)
        grid3.addWidget(QPushButton("T3 Second"), 1, 0)
        grid3.addWidget(QPushButton("T3 Third"), 2, 0)

class MyCell(QWidget):
    def __init__(self, address, server: MyModbusServer, is_holding_registers = True):
        super().__init__()
        self.server = server
        self.setFixedSize(160, 50)
        self.is_holding_registers = is_holding_registers
        # Set global font size
        font = QFont()
        font.setPointSize(15)
        self.setFont(font)
        self.address = address
        # Main layout
        main_layout = QGridLayout()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        self.label = QLabel("{:04d}".format(self.address))
        self.label.setFixedSize(50, 30)
        self.label.setMargin(0)
        self.edit = MyTextEdit(address, self.server, self.is_holding_registers)
        self.edit.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.edit.setFixedSize(90, 30)
        self.edit.setContentsMargins(QMargins(0, 0, 0, 0))
        main_layout.addWidget(self.label, 0, 0)
        main_layout.addWidget(self.edit, 0, 1)
        self.border_color = Qt.gray
        self.border_width = 3
        self.setContentsMargins(QMargins(0, 0, 0, 0))

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(self.border_color)
        pen.setWidth(self.border_width)
        painter.setPen(pen)
        painter.drawRect(
            0,
            0,
            self.width(),
            self.height()
        )

class MyTextEdit(QTextEdit):
    def __init__(self, address, server: MyModbusServer, is_holding_registers = True):
        super().__init__()
        self.server = server
        self.is_holding_registers = is_holding_registers
        self.address = address
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        text = self.toPlainText()
        value = self.try_int(text)
        if value is not None:
            if self.is_holding_registers:
                self.server.set_holding_registers(self.address, [value])
            else:
                self.server.set_input_registers(self.address, [value])

    def try_int(self, text):
        try:
            return int(text)
        except (ValueError, TypeError):
            return None

if __name__ == "__main__":
    CONFIG_PATH = Path("device.json")

    with CONFIG_PATH.open(encoding="utf-8") as f:
        CONFIG = json.load(f)

    IP_ADDRESS = CONFIG["ip"]
    PORT = CONFIG["port"]
    NUM_REGISTERS = CONFIG["num_of_registers"]
    START_ADDRESS = CONFIG["start_Address"]

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5() + """
        * {
            font-size: 17px;
        }
    """)
    window = MyMainWindow(IP_ADDRESS, PORT, NUM_REGISTERS, START_ADDRESS)
    window.setMinimumSize(1000, 800)
    window.show()
    sys.exit(app.exec_())


