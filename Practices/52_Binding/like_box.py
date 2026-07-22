import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QIcon

class CommandBinder:
    def __init__(self, command = None):
        self._callbacks = []
        if command :
            self._callbacks.append(command)

    def connect(self, callback):
        self._callbacks.append(callback)

    def invoke(self):
        for callback in self._callbacks:
            callback()

class IntegerBinder(QObject):

    viewChanged = pyqtSignal(int)
    viewModelChanged = pyqtSignal(int)

    def __init__(self, default = None):
        super().__init__()
        if default:
            self._value = default
        else:
            self._value = 0

    @property
    def value(self):
        return self._value
    
    def view_set_value(self, text):
        if self._value != text:
            self._value = text
            print(f"value changed from view: {self._value}")
            self.viewChanged.emit(self._value) # view -> view model signal 

    @value.setter
    def value(self, text):
        if self._value != text:
            self._value = text
            print(f"value changed from view model : {self._value}")
            self.viewModelChanged.emit(self._value) # view model -> view signal 

class MainViewModel():
    def __init__(self):
        self.like_count = IntegerBinder()
        self.like_count.value = 1
        self.like_click_binder = CommandBinder(self.on_like_button_pressed)
        self.hate_count = IntegerBinder()
        self.hate_count.value = 2
        self.hate_click_binder = CommandBinder(self.on_hate_button_pressed)

    def on_like_button_pressed(self):
        self.like_count.value = int(self.like_count.value) + 1

    def on_hate_button_pressed(self):
        self.hate_count.value = int(self.hate_count.value) + 1

class CustomTextBox(QLabel):

    textChanged = pyqtSignal(str)

    def __init__(self, binder : IntegerBinder, parent=None):
        super().__init__(parent)
        self.binder = binder
        self.setFixedSize(60, 30)
        self.setAlignment(Qt.AlignCenter)

        self.textChanged.connect(self.on_view_changed)
        self.binder.viewModelChanged.connect(self.on_view_model_changed)
        self.setText(str(self.binder.value))
        
    def setText(self, text):
        super().setText(str(text))
        self.textChanged.emit(str(text))

    def on_view_changed(self, text):
        if (self.binder):
            self.binder.view_set_value(text)

    def on_view_model_changed(self, text):
        self.blockSignals(True)
        self.setText(str(text))
        self.blockSignals(False)

class CustomButton(QPushButton):
    def __init__(self, command_binder : CommandBinder, parent = None):
        super().__init__()
        self.command_binder = command_binder
        self.setFixedSize(60, 50)
        self.clicked.connect(command_binder.invoke)

class MainView(QWidget):
    def __init__(self, view_model : MainViewModel, parent = None):
        super().__init__()
        self.view_model = view_model
        self.setFixedSize(200, 100)
        Hlayout = QHBoxLayout()
        Vlayout1 = QVBoxLayout()
        Vlayout2 = QVBoxLayout()
        Vlayout1.setSpacing(0)
        Vlayout2.setSpacing(0)

        self.like_count = CustomTextBox(self.view_model.like_count)
        self.like_button = CustomButton(self.view_model.like_click_binder)
        self.like_button.setIcon(QIcon("like.png"))

        Vlayout1.addWidget(self.like_count)
        Vlayout1.addWidget(self.like_button)

        self.hate_count = CustomTextBox(self.view_model.hate_count)
        self.hate_button = CustomButton(self.view_model.hate_click_binder)
        self.hate_button.setIcon(QIcon("hate.png"))

        Vlayout2.addWidget(self.hate_count)
        Vlayout2.addWidget(self.hate_button)

        Hlayout.addLayout(Vlayout1)
        Hlayout.addLayout(Vlayout2)
        self.setLayout(Hlayout)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Little like application")
        self.resize(400, 400)
        self.main_view_model = MainViewModel()
        self.main_view = MainView(self.main_view_model)
        self.setCentralWidget(self.main_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())