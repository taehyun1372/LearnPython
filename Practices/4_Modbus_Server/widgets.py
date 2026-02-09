from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from const import *
from utility import *
import threading
import time

class MainWindow(QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.setWindowTitle("PyQt Tabs with Buttons")
        self.setMinimumSize(400, 300)

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
        tabs.addTab(tab1, "IO")

        grid = QGridLayout()
        tab1.setLayout(grid)

        IO = IOWidget(self.client)
        grid.addWidget(IO, 0, 0)

        # --- Tab 2 ---
        tab2 = QWidget()
        tabs.addTab(tab2, "Tab 2")

        grid2 = QGridLayout()
        tab2.setLayout(grid2)

        grid2.addWidget(QPushButton("T2 Button A"), 0, 0)
        grid2.addWidget(QPushButton("T2 Button B"), 0, 1)
        grid2.addWidget(QPushButton("T2 Button C"), 1, 0)

        # --- Tab 3 ---
        tab3 = QWidget()
        tabs.addTab(tab3, "Tab 3")

        grid3 = QGridLayout()
        tab3.setLayout(grid3)

        grid3.addWidget(QPushButton("T3 First"), 0, 0)
        grid3.addWidget(QPushButton("T3 Second"), 1, 0)
        grid3.addWidget(QPushButton("T3 Third"), 2, 0)

class IOWidget(QWidget):
    def __init__(self, client, parent=None, default = []):
        super().__init__(parent)

        self.client = client
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel("PL01"), 0, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL01_PL02, 0, default=True), 0, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL01_PL02, 1, default=True), 0, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL01_PL02, 2, default=True), 0, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL01_PL02, 3, default=True), 0, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL01_PL02, 4, default=True), 0, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL01_PL02, 5, default=True), 0, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL01_PL02, 6), 0, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL01_PL02, 7), 0, 8)

        grid.addWidget(QLabel("PL02"), 1, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL01_PL02, 8), 1, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL01_PL02, 9), 1, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL01_PL02, 10), 1, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL01_PL02, 11), 1, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL01_PL02, 12), 1, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL01_PL02, 13), 1, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL01_PL02, 14), 1, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL01_PL02, 15), 1, 8)

        grid.addWidget(QLabel("PL03"), 2, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL03_PL04, 0), 2, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL03_PL04, 1), 2, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL03_PL04, 2), 2, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL03_PL04, 3), 2, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL03_PL04, 4), 2, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL03_PL04, 5), 2, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL03_PL04, 6), 2, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL03_PL04, 7), 2, 8)

        grid.addWidget(QLabel("PL04"), 3, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL03_PL04, 8), 3, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL03_PL04, 9), 3, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL03_PL04, 10), 3, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL03_PL04, 11), 3, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL03_PL04, 12), 3, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL03_PL04, 13), 3, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL03_PL04, 14), 3, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL03_PL04, 15), 3, 8)

        grid.addWidget(QLabel("PL05"), 4, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL05_PL06, 0), 4, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL05_PL06, 1), 4, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL05_PL06, 2), 4, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL05_PL06, 3), 4, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL05_PL06, 4), 4, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL05_PL06, 5), 4, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL05_PL06, 6), 4, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL05_PL06, 7), 4, 8)

        grid.addWidget(QLabel("PL06"), 5, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL05_PL06, 8), 5, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL05_PL06, 9), 5, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL05_PL06, 10), 5, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL05_PL06, 11), 5, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL05_PL06, 12), 5, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL05_PL06, 13), 5, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL05_PL06, 14), 5, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL05_PL06, 15), 5, 8)

        grid.addWidget(QLabel("PL07"), 6, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL07_PL08, 0), 6, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL07_PL08, 1), 6, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL07_PL08, 2), 6, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL07_PL08, 3), 6, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL07_PL08, 4), 6, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL07_PL08, 5), 6, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL07_PL08, 6), 6, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL07_PL08, 7), 6, 8)

        grid.addWidget(QLabel("PL08"), 7, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL07_PL08, 8), 7, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL07_PL08, 9), 7, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL07_PL08, 10), 7, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL07_PL08, 11), 7, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL07_PL08, 12), 7, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL07_PL08, 13), 7, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL07_PL08, 14), 7, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL07_PL08, 15), 7, 8)

        grid.addWidget(QLabel("PL07"), 8, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL07_PL08, 0), 8, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL07_PL08, 1), 8, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL07_PL08, 2), 8, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL07_PL08, 3), 8, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL07_PL08, 4), 8, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL07_PL08, 5), 8, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL07_PL08, 6), 8, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL07_PL08, 7), 8, 8)

        grid.addWidget(QLabel("PL08"), 9, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL07_PL08, 8), 9, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL07_PL08, 9), 9, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL07_PL08, 10), 9, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL07_PL08, 11), 9, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL07_PL08, 12), 9, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL07_PL08, 13), 9, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL07_PL08, 14), 9, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL07_PL08, 15), 9, 8)

        grid.addWidget(QLabel("PL09"), 10, 0)
        grid.addWidget(DigitalButton("Pin01", self.client, IN_PL09_PL10, 0, default=True), 10, 1)
        grid.addWidget(DigitalButton("Pin02", self.client, IN_PL09_PL10, 1, default=True), 10, 2)
        grid.addWidget(DigitalButton("Pin03", self.client, IN_PL09_PL10, 2, default=True), 10, 3)
        grid.addWidget(DigitalButton("Pin04", self.client, IN_PL09_PL10, 3), 10, 4)
        grid.addWidget(DigitalButton("Pin05", self.client, IN_PL09_PL10, 4, default=True), 10, 5)
        grid.addWidget(DigitalButton("Pin06", self.client, IN_PL09_PL10, 5), 10, 6)
        grid.addWidget(DigitalButton("Pin07", self.client, IN_PL09_PL10, 6), 10, 7)
        grid.addWidget(DigitalButton("Pin08", self.client, IN_PL09_PL10, 7), 10, 8)

        threading.Thread(target=self.IO_simulation, daemon=True).start()

    def IO_simulation(self):
        while (True):
            PL03_04_Out = read_register(self.client, 60109)
            PL03_04_In = read_register(self.client, 60101)
            PL07_08_In = read_register(self.client, 60103)

            gatevalve_open = get_bit(PL03_04_Out, 8)
            bypass_online = get_bit(PL03_04_Out, 11)
            MVU_open = get_bit(PL03_04_Out, 12)
            MVL_open = get_bit(PL03_04_Out, 13)

            if gatevalve_open:
                PL03_04_In = set_bit(PL03_04_In, True, 0)
                PL03_04_In = set_bit(PL03_04_In, False, 1)
            else:  # Bypass Valve Bypass command
                PL03_04_In = set_bit(PL03_04_In, False, 0)
                PL03_04_In = set_bit(PL03_04_In, True, 1)

            if bypass_online :  # Bypass Valve Online command
                PL03_04_In = set_bit(PL03_04_In, True, 6)
                PL03_04_In = set_bit(PL03_04_In, False, 7)
            else:  # Bypass Valve Bypass command
                PL03_04_In = set_bit(PL03_04_In, False, 6)
                PL03_04_In = set_bit(PL03_04_In, True, 7)

            if MVU_open:
                PL07_08_In = set_bit(PL07_08_In, True, 0)
                PL07_08_In = set_bit(PL07_08_In, False, 1)
            else:
                PL07_08_In = set_bit(PL07_08_In, False, 0)
                PL07_08_In = set_bit(PL07_08_In, True, 1)

            if MVL_open:
                PL07_08_In = set_bit(PL07_08_In, True, 2)
                PL07_08_In = set_bit(PL07_08_In, False, 3)
            else:
                PL07_08_In = set_bit(PL07_08_In, False, 2)
                PL07_08_In = set_bit(PL07_08_In, True, 3)

            write_register(self.client,60101, PL03_04_In)
            write_register(self.client, 60103, PL07_08_In)


class DigitalButton(QPushButton):
    def __init__(self, text, client, word, bit, default=False):
        super().__init__(text)
        self.client = client
        self.word = word
        self.bit = bit
        self.clicked.connect(self.toggle)
        self._status = False
        self.setStyleSheet("background-color: gray; color: white;")

        if default:
            self.set()

    def toggle(self):
        if self._status == False:
            self.set()
        else:
            self.reset()

    def set(self):
        set_register_bit(self.client, self.word, self.bit)
        self.setStyleSheet("background-color: green; color: white;")

    def set_callback(self):
        self._status = True


    def reset(self):
        reset_register_bit(self.client, self.word, self.bit)
        self.setStyleSheet("background-color: gray; color: white;")

    def reset_callback(self):
        self._status = False

