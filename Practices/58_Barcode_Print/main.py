import sys
from PyQt6.QtWidgets import (
    QLabel,
    QApplication,
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton
)
from dataclasses import dataclass
import json
from pathlib import Path
import socket

@dataclass
class Config:
    label_definition : str
    material_printer : str
        

class MyDialog(QDialog):
    def __init__(self, config : Config):
        super().__init__()
        self.config = config
        self.ip_address = self.config.material_printer
        self.setWindowTitle("Barcode Print")

        # 위젯 생성
        self.label = QLabel("Print label")
        self.label.setObjectName("titleLabel")
        self.textbox = QLineEdit()
        self.button = QPushButton("Submit")

        # 버튼 이벤트 연결
        self.button.clicked.connect(self.on_button_clicked)

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)

        self.setLayout(layout)
        
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            
            QLabel#titleLabel {
                color: #1f2328;
                font-size: 18px;
                font-weight: 600;
                padding-bottom: 5px;
            }

            QLineEdit {
                border: 2px solid #d0d7de;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #4a90e2;
            }

            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #357abd;
            }

            QPushButton:pressed {
                background-color: #2d66a3;
            }
        """)
        
        self.template = Path(Path(__file__).parent / self.config.label_definition).read_text(encoding="utf-8")
    

    def on_button_clicked(self):
        container_name = self.textbox.text()
        zpl = self.template.replace("$ContainerName$",container_name)
        self.print_zpl(zpl)
    
    def print_zpl(self, zpl):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self.ip_address, 9100))
            sock.sendall(zpl.encode("utf-8"))
        finally:
            sock.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config_path = Path(__file__).parent / "config.json"
    
    with open(config_path, "r") as f:
        data = json.load(f)

    config = Config(**data)
    
    dlg = MyDialog(config)
    dlg.show()

    sys.exit(app.exec())