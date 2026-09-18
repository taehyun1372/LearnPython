from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QProgressBar, QPushButton
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central = QWidget()
        layout = QGridLayout()
        
        self.description = QLabel("Progress bar")
        self.progress = QProgressBar()
        self.progress.setValue(15)
        self.progress.setStyleSheet("""
            QProgressBar {
            border: none;
            border-radius: 6px;
            text-align: center;
            background-color: #E5E7EB;
            color: black;
            height: 20px;
            }
            
            QProgressBar::chunk {
            border-radius: 6px;
            background-color: #3B82F6;
            }
            """)
        
        self.btn_increase = QPushButton("Increase")
        self.btn_decrease= QPushButton("Decrease")
        self.btn_increase.clicked.connect(self.increase)
        self.btn_decrease.clicked.connect(self.decrease)
        
        layout.addWidget(self.description, 0, 0)
        layout.addWidget(self.progress, 0, 1)
        
        layout.addWidget(self.btn_increase, 1, 0)
        layout.addWidget(self.btn_decrease, 1, 1)
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        
    def increase(self):
        value = self.progress.value()
        self.progress.setValue(min(100, value + 10))
        
    def decrease(self):
        value = self.progress.value()
        self.progress.setValue(max(0, value - 10))
        
    
if __name__ == "__main__":
    print("something")
    app = QApplication(sys.argv)
    main = MyMainWindow()
    main.show()
    app.exec()