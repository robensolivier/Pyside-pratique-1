import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class Calculatrice(QMainWindow):
    def __init__(self):
        super().__init__()
        # Charger l'interface
        loader = QUiLoader()
        self.ui = loader.load("calculatrice.ui", self)
        
        self.setCentralWidget(self.ui.centralwidget)
        
        # Connecter les boutons
        self.ui.calculerButton.clicked.connect(self.calculer)
        self.ui.annulerButton.clicked.connect(self.annuler)
        
    def calculer(self):
        try:
            a = float(self.ui.aLineEdit.text())
            b = float(self.ui.bLineEdit.text())
            self.ui.sommeLineEdit.setText(str(a + b))
        except:
            self.ui.sommeLineEdit.setText("Erreur")
    
    def annuler(self):
        self.ui.aLineEdit.clear()
        self.ui.bLineEdit.clear()
        self.ui.sommeLineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculatrice()
    window.show()
    sys.exit(app.exec()) 