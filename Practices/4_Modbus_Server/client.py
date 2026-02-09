from pymodbus.client.sync import ModbusUdpClient
import logging
import threading
import time
import multiprocessing
import os
import sys
from const import *
from widgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import qdarkstyle

if __name__ == "__main__":
    client = ModbusUdpClient(EXP_MASTER_IP, port=PORT)

    # Connect
    client.connect()
    print("PLC connected")

    print("Initializing IO data")
    client.write_registers(SIMULATION_OFFSET + 0, [0] * SIMULATION_IO_SIZE)

    # Writing simulation data
    client.write_register(SIMULATION_OFFSET + 0, SIMULATION_PASSWORD_H)
    client.write_register(SIMULATION_OFFSET + 59, SIMULATION_PASSWORD_L)

    print("Enabling simulation mode")

    client.close()

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5() + """
    * {
        font-size: 17px;
    }
""")

    window = MainWindow(client)
    window.show()
    sys.exit(app.exec_())