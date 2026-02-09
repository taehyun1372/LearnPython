import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QPushButton, QWidget, QTextEdit


class DataModel(QObject):
    changed = pyqtSignal(str)
    reset = pyqtSignal()

    def __init__(self, value = 0):
        super().__init__()
        self._value = 0
        self.set(value)


    def set(self, value):
        if self._value != value:
            self._value = value
            self.changed.emit(str(value))

    def value(self):
        return self._value

class MyLabel(QLabel):
    def __init__(self, value):
        super().__init__()
        self._data = DataModel()
        self._data.changed.connect(self.setText)
        self._data.set(value)

    def data(self):
        return self._data

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        main_grid = QGridLayout()

        self.setLayout(main_grid)

        input1 = QTextEdit()
        input2 = QTextEdit()
        input3 = QTextEdit()
        input4 = QTextEdit()
        input5 = QTextEdit()

        input1.textChanged.connect(self.on_text_changed)
        input2.textChanged.connect(self.on_text_changed)
        input3.textChanged.connect(self.on_text_changed)
        input4.textChanged.connect(self.on_text_changed)
        input5.textChanged.connect(self.on_text_changed)

        main_grid.addWidget(input1, 0, 0)
        main_grid.addWidget(input2, 0, 1)
        main_grid.addWidget(input3, 0, 2)
        main_grid.addWidget(input4, 0, 3)
        main_grid.addWidget(input5, 0, 4)


        self._data = [1, 2, 3, 4, 5]

        label1 = MyLabel(1)
        label2 = MyLabel(2)
        label3 = MyLabel(3)
        label4 = MyLabel(4)
        label5 = MyLabel(5)

        self._labels = []
        self._labels.append(label1)
        self._labels.append(label2)
        self._labels.append(label3)
        self._labels.append(label4)
        self._labels.append(label5)

        main_grid.addWidget(label1, 1, 0)
        main_grid.addWidget(label2, 2, 0)
        main_grid.addWidget(label3, 3, 0)
        main_grid.addWidget(label4, 4, 0)
        main_grid.addWidget(label5, 5, 0)

    def set_data(self, index, value):
        if len(self._data) > index > 0:
            if self._data[index] != value:
                self._data[index] = value
                self._labels[index].data().set(value)


    def on_text_changed(self):
        textEdit = self.sender()
        text = textEdit.toPlainText()
        try:
            value = int(text)
        except Exception as e:
            print("fail to cast")


        print()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
