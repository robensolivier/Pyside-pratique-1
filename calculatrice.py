import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Calculatrice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setFixedSize(400, 300)
        self.setup_ui()
        
    def setup_ui(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Titre
        title_label = QLabel("Calculatrice")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: red; margin: 20px;")
        main_layout.addWidget(title_label)
        
        # Layout pour les champs de saisie
        input_layout = QVBoxLayout()
        
        # Champ a
        a_layout = QHBoxLayout()
        a_label = QLabel("a=")
        a_label.setFont(QFont("Arial", 14))
        a_label.setStyleSheet("color: blue; font-weight: bold;")
        self.a_input = QLineEdit()
        self.a_input.setFixedHeight(30)
        a_layout.addWidget(a_label)
        a_layout.addWidget(self.a_input)
        input_layout.addLayout(a_layout)
        
        # Champ b
        b_layout = QHBoxLayout()
        b_label = QLabel("b=")
        b_label.setFont(QFont("Arial", 14))
        b_label.setStyleSheet("color: blue; font-weight: bold;")
        self.b_input = QLineEdit()
        self.b_input.setFixedHeight(30)
        b_layout.addWidget(b_label)
        b_layout.addWidget(self.b_input)
        input_layout.addLayout(b_layout)
        
        # Champ somme
        somme_layout = QHBoxLayout()
        somme_label = QLabel("Somme=")
        somme_label.setFont(QFont("Arial", 14))
        somme_label.setStyleSheet("color: blue; font-weight: bold;")
        self.somme_input = QLineEdit()
        self.somme_input.setFixedHeight(30)
        self.somme_input.setReadOnly(True)  # Lecture seule pour le résultat
        self.somme_input.setStyleSheet("background-color: #f0f0f0;")
        somme_layout.addWidget(somme_label)
        somme_layout.addWidget(self.somme_input)
        input_layout.addLayout(somme_layout)
        
        main_layout.addLayout(input_layout)
        
        # Layout pour les boutons
        button_layout = QHBoxLayout()
        
        # Bouton Calculer
        self.calculer_button = QPushButton("Calculer")
        self.calculer_button.setFixedSize(100, 40)
        self.calculer_button.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                border: 2px solid #808080;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)
        self.calculer_button.clicked.connect(self.calculer)
        
        # Bouton Annuler
        self.annuler_button = QPushButton("Annuler")
        self.annuler_button.setFixedSize(100, 40)
        self.annuler_button.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                border: 2px solid #808080;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)
        self.annuler_button.clicked.connect(self.annuler)
        
        button_layout.addWidget(self.calculer_button)
        button_layout.addWidget(self.annuler_button)
        button_layout.setAlignment(Qt.AlignCenter)
        
        main_layout.addLayout(button_layout)
        main_layout.addStretch()  # Ajouter de l'espace en bas
        
    def calculer(self):
        try:
            # Récupérer les valeurs des champs a et b
            a_text = self.a_input.text().strip()
            b_text = self.b_input.text().strip()
            
            if not a_text or not b_text:
                self.somme_input.setText("Erreur: Veuillez saisir les deux nombres")
                return
            
            # Convertir en nombres
            a = float(a_text)
            b = float(b_text)
            
            # Calculer la somme
            somme = a + b
            
            # Afficher le résultat
            if somme == int(somme):
                self.somme_input.setText(str(int(somme)))
            else:
                self.somme_input.setText(str(somme))
                
        except ValueError:
            self.somme_input.setText("Erreur: Nombres invalides")
    
    def annuler(self):
        # Vider tous les champs
        self.a_input.clear()
        self.b_input.clear()
        self.somme_input.clear()

def main():
    app = QApplication(sys.argv)
    
    # Créer et afficher la fenêtre
    calculatrice = Calculatrice()
    calculatrice.show()
    
    # Lancer la boucle d'événements
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 