
from pymodbus.client.sync import ModbusTcpClient, BaseModbusClient
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

from pymodbus.utilities import ModbusTransactionState


class MyMainWindow(QWidget):
    def __init__(self, ip_address, port, unit = 1):
        super().__init__()
        self.setWindowTitle("PyQt Modbus Client")
        self.ip_address = ip_address
        self.port = port
        self.client = ModbusTcpClient(self.ip_address, self.port)
        self.unit = unit
        self.holding_register_start_address = 0
        self.input_register_start_address = 0
        self.number_of_registers = 100

        # Connect
        self.client.connect()
        print("PLC connected")

        self.setMinimumSize(600, 800)

        # Set global font size
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        button_box = QHBoxLayout()
        self.connect_button = QPushButton("connect")
        self.connect_button.setStyleSheet("""
        QPushButton {
            background-color: green;
            color: white;
        }
        """)
        self.connect_button.clicked.connect(self.connect)
        self.disconnect_button = QPushButton("disconnect")
        self.disconnect_button.clicked.connect(self.disconnect)
        self.ip_address_input = QTextEdit(self.ip_address)
        self.ip_address_input.textChanged.connect(self.set_ip_address)
        self.ip_address_input.setFixedSize(120, 40)
        self.port_input = QTextEdit(str(self.port))
        self.port_input.textChanged.connect(self.set_port)
        self.port_input.setFixedSize(80, 40)
        self.unit_input = QTextEdit(str(self.unit))
        self.unit_input.setFixedSize(80, 40)

        button_box.addWidget(self.connect_button)
        button_box.addWidget(self.disconnect_button)
        button_box.addWidget(self.ip_address_input)
        button_box.addWidget(self.port_input)
        button_box.addWidget(self.unit_input)


        main_layout.addLayout(button_box)

        # --- Create Tab Control ---
        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        # --- Tab 1 ---
        tab1 = QWidget()
        tabs.addTab(tab1, "Holding Registers")
        tab1_layout = QVBoxLayout(tab1)

        holding_button_box = QHBoxLayout()
        self.set_holding_start_address = QPushButton("Set Start Address")
        self.set_holding_start_address.setFixedSize(120, 28)
        self.set_holding_start_address.clicked.connect(self.on_holding_start_address_clicked)
        self.holding_start_address_input = QTextEdit("0")
        self.holding_start_address_input.setFixedSize(120, 28)
        holding_button_box.addWidget(self.set_holding_start_address)
        holding_button_box.addWidget(self.holding_start_address_input)

        tab1_layout.addLayout(holding_button_box)

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

        self._holding_cells = []
        for j in range(10):
            for i in range(10):
                cell = MyCell(j*10 + i)
                self._holding_cells.append(cell)
                grid1.addWidget(cell, i, j)


        # --- Tab 2 ---
        tab2 = QWidget()
        tabs.addTab(tab2, "Input Registers")
        tab2_layout = QVBoxLayout(tab2)

        input_button_box = QHBoxLayout()
        self.set_input_start_address = QPushButton("Set Start Address")
        self.set_input_start_address.setFixedSize(120, 28)
        self.set_input_start_address.clicked.connect(self.on_input_start_address_clicked)
        self.input_start_address_input = QTextEdit("0")
        self.input_start_address_input.setFixedSize(120, 28)
        input_button_box.addWidget(self.set_input_start_address)
        input_button_box.addWidget(self.input_start_address_input)

        tab2_layout.addLayout(input_button_box)

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

        self._input_cells = []
        for j in range(10):
            for i in range(10):
                cell = MyCell(j*10 + i)
                self._input_cells.append(cell)
                grid2.addWidget(cell, i, j)

        self.h_th = threading.Thread(target = self.holding_register_monitoring, daemon=True)
        self.h_th.start()

        self.i_th = threading.Thread(target = self.input_register_monitoring, daemon=True)
        self.i_th.start()

    def on_holding_start_address_clicked(self):
        text = self.holding_start_address_input.toPlainText()
        try:
            value = int(text)
            self.holding_register_start_address = value
            for i, cell in enumerate(self._holding_cells):
                cell.set_address(self.holding_register_start_address + i)
        except Exception as e:
            print("failed to set holding register start address")

    def on_input_start_address_clicked(self):
        text = self.input_start_address_input.toPlainText()
        try:
            value = int(text)
            self.input_register_start_address = value
            for i, cell in enumerate(self._input_cells):
                cell.set_address(self.input_register_start_address + i)
        except Exception as e:
            print("failed to set input register start address")

    def connect(self):
        self.client = ModbusTcpClient(self.ip_address, self.port)
        self.client.connect()
        print("PLC Connected")
        self.connect_button.setStyleSheet("""
        QPushButton {
            background-color: green;
            color: white;
        }
        """)

        try:
            text = self.unit_input.toPlainText()
            value = int(text)
            self.unit = value
        except Exception as e:
            print("fail to set unit id {}".format(e))

        try:
            if self.h_th is None or not self.h_th.is_alive():
                self.h_th = threading.Thread(target=self.holding_register_monitoring, daemon=True)
                self.h_th.start()
                print("Starting holding register thread again")
            if self.i_th is None or not self.i_th.is_alive():
                self.i_th = threading.Thread(target=self.input_register_monitoring, daemon=True)
                self.i_th.start()
                print("Starting input register thread again")
        except Exception as e:
            print("fail to start monitoring service again {}".format(e))

    def disconnect(self):
        self.client.close()
        print("PLC Disconnected")
        self.connect_button.setStyleSheet("""
        QPushButton {
            background-color: gray;
            color: white;
        }
        """)

    def set_ip_address(self):
        text = self.sender().toPlainText()
        print("IP address changed to {}".format(text))
        self.ip_address = text

    def set_port(self):
        text = self.sender().toPlainText()
        print("Port changed to {}".format(text))
        try:
            value = int(text)
            self.port = value
        except Exception as e:
            print("fail to update port to {}".format(text))


    def holding_register_monitoring(self):
        while True:
            hr = self.client.read_holding_registers(self.holding_register_start_address, self.number_of_registers, unit=self.unit)
            if hr.isError():
                print(hr)
            else:
                value = hr.registers
                for i in range(len(value)):
                    self._holding_cells[i].update_value(value[i])

            time.sleep(1)

    def input_register_monitoring(self):
        while True:
            hr = self.client.read_input_registers(self.input_register_start_address, self.number_of_registers, unit=self.unit)
            if hr.isError():
                print(hr)
            else:
                value = hr.registers
                for i in range(len(value)):
                    self._input_cells[i].update_value(value[i])

            time.sleep(1)

class MyCell(QWidget):
    valueChanged = pyqtSignal(str)

    def __init__(self, address):
        super().__init__()
        self.setFixedSize(160, 50)
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
        self.edit = MyTextEdit(address)
        self.edit.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.edit.setFixedSize(90, 30)
        self.edit.setContentsMargins(QMargins(0, 0, 0, 0))
        main_layout.addWidget(self.label, 0, 0)
        main_layout.addWidget(self.edit, 0, 1)
        self.border_color = Qt.darkCyan
        self.border_width = 3
        self.setContentsMargins(QMargins(0, 0, 0, 0))
        self.valueChanged.connect(self.setText)

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

    def setText(self, text):
        if text != self.edit.toPlainText():
            self.edit.setText(text)

    def update_value(self, value):
        self.valueChanged.emit(str(value))

    def set_address(self, address):
        self.label.setText("{:04d}".format(address))

class MyTextEdit(QTextEdit):
    def __init__(self, address):
        super().__init__()
        self.address = address
        self.setText(str(0))

if __name__ == "__main__":
    CONFIG_PATH = Path("device.json")

    with CONFIG_PATH.open(encoding="utf-8") as f:
        CONFIG = json.load(f)

    IP_ADDRESS = CONFIG["ip"]
    PORT = CONFIG["port"]
    UNIT_ID = CONFIG["unit_id"]

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5() + """
    * {
        font-size: 17px;
    }
""")

    window = MyMainWindow(IP_ADDRESS, PORT, UNIT_ID)
    window.setMinimumSize(1000, 800)
    window.show()
    sys.exit(app.exec_())