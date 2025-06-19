import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello App')
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(500, 350)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.inputField = QLineEdit()
        self.button = QPushButton('Say hello')
        self.button.clicked.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)   
        layout.addWidget(self.button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText(f'Hello {inputText}')

app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 20px;
    }
    QPushButton {
        font-size: 25px;
    }
''')

window = MyApp()
window.show()
app.exec()