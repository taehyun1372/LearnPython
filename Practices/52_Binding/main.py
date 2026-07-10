import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject

class TextBinder(QObject):

    viewChanged = pyqtSignal(str)
    viewModelChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._value = ""

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

class BindLineEdit(QLineEdit):

    def __init__(self, text_binder: TextBinder):
        super().__init__()
        self.text_binder = text_binder

        self._value = ""
        self.textChanged.connect(self.on_view_changed)
        self.text_binder.viewModelChanged.connect(self.on_view_model_changed)

    def on_view_changed(self, text):
        if (self.text_binder):
            self.text_binder.view_set_value(text)

    def on_view_model_changed(self, text):
        self.blockSignals(True)
        self.setText(text)
        self.blockSignals(False)

class UserViewModel():
    def __init__(self):
        self.name = TextBinder()
        self.age = TextBinder()
        self.output = TextBinder()

        self.name.viewChanged.connect(self.on_name_view_changed)
        self.age.viewChanged.connect(self.on_age_view_changed)
        self.output.value = "Text"

    def on_name_view_changed(self, name):
        print(f"Info : name changed to {name}")

    def on_age_view_changed(self, age):
        print(f"Info : age changed to {age}")

class UserView(QWidget):
    def __init__(self, view_model : UserViewModel):
        super().__init__()
        self.view_model = view_model

        # Layout
        # Widgets
        self.name_edit = BindLineEdit(self.view_model.name)
        self.name_edit.setPlaceholderText("Enter your name")

        self.age_edit = BindLineEdit(self.view_model.age)
        self.age_edit.setPlaceholderText("Enter your age")

        self.output = BindLineEdit(self.view_model.output)
        self.output.setReadOnly(True)

        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Age"))
        layout.addWidget(self.age_edit)

        layout.addWidget(self.submit_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.output)

        self.setLayout(layout)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple PyQt Example")
        self.resize(400, 300)

        self.user_view_model = UserViewModel()
        self.user_view = UserView(self.user_view_model)
        self.setCentralWidget(self.user_view)

        self.user_view_model.name.value = "Roy"
        self.user_view_model.age.value = "38"
        self.user_view_model.output.value = "set some value"

        # # Events
        # self.submit_button.clicked.connect(self.submit)
        # self.clear_button.clicked.connect(self.clear)

    # def submit(self):
    #     name = self.name_edit.text()
    #     age = self.age_edit.text()

    #     self.output.append(f"Name: {name}")
    #     self.output.append(f"Age: {age}")
    #     self.output.append("----------------")

    # def clear(self):
    #     self.name_edit.clear()
    #     self.age_edit.clear()
    #     self.output.clear()


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())