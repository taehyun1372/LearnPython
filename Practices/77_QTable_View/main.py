from PyQt6.QtWidgets import QAbstractItemView, QPushButton, QHeaderView, QApplication, QMainWindow, QTableView, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QColor, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowTitle = "Q Table View"
        central = QWidget()
        layout = QGridLayout()
        self.label = QLabel()
        self.update_label("Test result")
        self.table = QTableView()
        self.model = QStandardItemModel()
        self.btn_remove_current_row = QPushButton("Remove Current")
        self.btn_remove_all_row = QPushButton("Remove All")
        
        self.btn_remove_current_row.clicked.connect(self.remove_current_row)
        self.btn_remove_all_row.clicked.connect(self.remove_all_row)
        
        self.table.setModel(self.model)
        layout.addWidget(self.label, 0, 0, 1, 3)
        layout.addWidget(self.table, 1, 0, 1, 3)
        layout.addWidget(self.btn_remove_current_row, 2, 0)
        layout.addWidget(self.btn_remove_all_row, 2, 1)
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.initialize_table()
        self.add_row(1, "connect rtt", "pass")
        self.add_row(2, "reboot MCU", "pass")
        self.add_row(3, "flash firmware", "failed")
        
        data = [
            [1, "DMS", "PASS"],
            [2, "ICP", "FAIL"],
            [3, "FLASHING", "PASS"]
        ]
        self.bulk_update(data)
        
    def initialize_table(self):
        headers = [
            "Name",
            "Version",
            "Status",
            "Result"
        ]
        self.model.setHorizontalHeaderLabels(headers)
        self.model.setColumnCount(7)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 60)
        self.table.setColumnWidth(2, 60)
        self.table.setColumnWidth(3, 60)
        self.table.setColumnWidth(4, 20)
        self.table.setColumnWidth(5, 20)
        self.table.setColumnWidth(6, 20)
        self.table.hideColumn(4)
        self.table.hideColumn(5)
        self.table.hideColumn(6)
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSortingEnabled(True)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        self.table.setStyleSheet("""
        QTableView {
            gridline-color: gray;
            selection-background-color: #0078D4;
        }

        QHeaderView::section {
            background-color: #404040;
            color: white;
            font-weight: bold;
        }
        """)
        
    def add_row(self, index: int, name: str, result: str):
        result_item = QStandardItem(result)
        if result.upper() == "PASS":
            result_item.setBackground(QColor("#C6EFCE"))
        else:
            result_item.setBackground(QColor("#FFC7CE"))
        
        result_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        row = [
            QStandardItem(index),
            QStandardItem(name),
            result_item
        ]
        
        self.model.appendRow(row)
        count = self.model.rowCount()
        last_item = self.model.item(count - 1, 1)
        message = f"total count - {count}, last item - {last_item.text()}"
        self.update_label(message)
        
    def update_label(self, message):
        self.label.setText(message)
        
    def remove_current_row(self):
        row_index = self.table.currentIndex().row()
        self.model.removeRow(row_index)
    
    def remove_all_row(self):
        self.model.removeRows(0, self.model.rowCount())
        
    def bulk_update(self, data):
        for row_data in data:
            items = [
                QStandardItem(str(x)) for x in row_data
            ]
            self.model.appendRow(items)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
