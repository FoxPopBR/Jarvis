import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                               QVBoxLayout, QWidget, QLabel, QSpacerItem, 
                               QSizePolicy, QFrame)
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QIcon, QPalette, QColor

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurações da janela principal
        self.setWindowTitle('Menu Principal - Senhor Fox')
        self.setWindowIcon(QIcon('path_to_your_icon.png'))  # Adicione o caminho para o ícone da janela
        self.setGeometry(100, 100, 1280, 720)  # Tamanho inicial da janela
        self.setMinimumSize(1280, 720)  # Tamanho mínimo da janela

        # Aplica um tema escuro à aplicação
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)

        # Layout principal
        layout = QVBoxLayout()

        # Painel centralizado para os botões
        button_panel = QFrame(self)
        button_panel.setFrameShape(QFrame.StyledPanel)
        button_panel.setPalette(palette)
        button_panel_layout = QVBoxLayout(button_panel)
        button_panel_layout.setSpacing(10)  # Espaçamento entre os botões
        button_panel_layout.setContentsMargins(20, 20, 20, 20)  # Margens internas do painel

        # Botão Chatbot
        self.chatbot_button = QPushButton('Chatbot', button_panel)
        self.chatbot_button.setFont(QFont('Arial', 16))
        button_panel_layout.addWidget(self.chatbot_button)

        # Botão Configurações
        self.settings_button = QPushButton('Configurações', button_panel)
        self.settings_button.setFont(QFont('Arial', 16))
        button_panel_layout.addWidget(self.settings_button)

        # Botão Sair
        self.exit_button = QPushButton('Sair', button_panel)
        self.exit_button.setFont(QFont('Arial', 16))
        self.exit_button.clicked.connect(self.close)  # Conecta o botão à função de fechar a janela
        button_panel_layout.addWidget(self.exit_button)

        # Adiciona o painel de botões ao layout principal
        layout.addWidget(button_panel, 0, Qt.AlignCenter)

        # Widget central que contém o layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Inicializa a aplicação e cria a janela
app = QApplication(sys.argv)
main_menu = MainMenu()
main_menu.show()
sys.exit(app.exec_())
