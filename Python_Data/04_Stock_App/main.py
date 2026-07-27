import sys
import yfinance as yf

from PyQt6.QtWidgets import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt6.QtCore import QDate

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(111)

        super().__init__(self.fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_date = QDate.currentDate().toString("yyyy-MM-dd")
        self.end_date = QDate.currentDate().toString("yyyy-MM-dd")
        self.ticker = ""

        self.canvas = MplCanvas()
        self.main = QWidget()
        layout = QVBoxLayout()

        self.ticker_label = QLineEdit("ticker")
        self.ticker_label.textChanged.connect(self.ticker_changed)

        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)  # 클릭하면 달력 표시
        self.start_date_edit.setDate(QDate.currentDate())
        self.start_date_edit.dateChanged.connect(self.start_date_changed)

        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)  # 클릭하면 달력 표시
        self.end_date_edit.setDate(QDate.currentDate())
        self.end_date_edit.dateChanged.connect(self.end_date_changed)

        self.query_button = QPushButton()
        self.query_button.clicked.connect(self.query_button_pressed)

        layout.addWidget(self.ticker_label)
        layout.addWidget(self.start_date_edit)
        layout.addWidget(self.end_date_edit)
        layout.addWidget(self.query_button)

        samsung_stock = yf.download(
            "005930.KS",
            start="2026-07-01",
            end="2026-07-27"
        )

        del samsung_stock["Open"]
        del samsung_stock["High"]
        del samsung_stock["Low"]
        del samsung_stock["Volume"]

        self.canvas.ax.plot(samsung_stock)
        self.canvas.draw()

        layout.addWidget(self.canvas)
        self.main.setLayout(layout)
        self.setCentralWidget(self.main)

    def start_date_changed(self, date : QDate):
        self.start_date = date.toString("yyyy-MM-dd")

    def end_date_changed(self, date : QDate):
        self.end_date = date.toString("yyyy-MM-dd")

    def ticker_changed(self, ticker : str):
        self.ticker = ticker

    def query_button_pressed(self):
        samsung_stock = yf.download(
            self.ticker,
            start=self.start_date,
            end=self.end_date
        )

        self.canvas.ax.clear()

        del samsung_stock["Open"]
        del samsung_stock["High"]
        del samsung_stock["Low"]
        del samsung_stock["Volume"]

        self.canvas.ax.plot(samsung_stock)
        self.canvas.draw()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()