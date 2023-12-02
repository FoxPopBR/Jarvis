from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from .widgets import CustomWidgetFactory
from ..config import WindowManager  
from Jarvis_Alfa.screen import ScreenManager  # Atualizada a importação

class LayoutManager:
    @staticmethod
    def center_window_on_screen():
        """Centraliza a janela na tela."""
        try:
            WindowManager.center_window_on_screen()  # Usando o método da WindowManager

        except Exception as e:
            print(f"Erro ao centralizar janela: {e}")

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        spacer_left = Widget(size_hint_x=1)
        spacer_right = Widget(size_hint_x=1)

        button = self.create_hello_button()

        self.add_widget(spacer_left)
        self.add_widget(button)
        self.add_widget(spacer_right)

    def create_hello_button(self):
        """Cria um botão de saudação."""
        button = CustomWidgetFactory.create_centered_button(
            text='Hello, Senhor Fox',
            size=(200, 40),
            on_press=self.hello_button_pressed
        )
        return button

    def hello_button_pressed(self, instance):
        """Lógica quando o botão de saudação é pressionado."""
        print("Botão de Saudação Pressionado")
        # Adicione sua lógica específica aqui, por exemplo, navegar para outra tela
        screen_manager = ScreenManager()  # Criando uma instância do gerenciador de tela
        screen_manager.show_menu()  # Exibindo o menu

def create_main_layout():
    """Cria o layout principal da aplicação, centralizado na tela."""
    LayoutManager.center_window_on_screen()  # Centralizando a janela
    main_layout = MainLayout()
    Clock.schedule_once(lambda dt: ScreenManager().show_menu(), 0.1)
    return main_layout
