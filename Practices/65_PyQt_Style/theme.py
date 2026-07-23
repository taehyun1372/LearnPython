import sys
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet, list_themes

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        layout = QVBoxLayout()

        lbName = QLabel("Name")
        btnName = QPushButton()

        lbAge = QLabel("Age")
        btnAge = QPushButton()

        lbGender = QLabel("Gender")
        btnGender = QPushButton()

        explorer = MyExplorer()

        progress = MyProgressBar()

        layout.addWidget(lbName)
        layout.addWidget(btnName)
        layout.addWidget(lbAge)
        layout.addWidget(btnAge)
        layout.addWidget(lbGender)
        layout.addWidget(btnGender)
        layout.addWidget(explorer)
        layout.addWidget(progress)

        centralWidget.setLayout(layout)
        
        self.setCentralWidget(centralWidget)


class MyExplorer(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("No file selected")

        button = QPushButton("Browse...")
        button.clicked.connect(self.browse_file)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(button)

    def browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "All Files (*.*)"
        )

        if filename:
            self.label.setText(filename)

class MyProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)

        btnIncrease = QPushButton("Increase")
        btnIncrease.clicked.connect(self.increase_progress)

        btnDecrease = QPushButton("Decrease")
        btnDecrease.clicked.connect(self.decrease_progress)

        layout = QVBoxLayout(self)
        layout.addWidget(self.progress)
        layout.addWidget(btnIncrease)
        layout.addWidget(btnDecrease)


    def increase_progress(self):
        value = self.progress.value()
        self.progress.setValue(min(value + 10, 100))

    def decrease_progress(self):
        value = self.progress.value()
        self.progress.setValue(max(value - 10, 0))

if __name__ == "__main__":
    print(list_themes())
    app = QApplication(sys.argv)
    myWindow = MyMainWindow()
    myWindow.show()
    apply_stylesheet(app, theme='light_teal_500.xml')
    sys.exit(app.exec_())
