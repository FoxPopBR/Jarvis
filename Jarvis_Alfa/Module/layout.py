from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button  # Importação da classe Button
from kivy.core.window import Window
from .widgets import CenteredButton  # Importação relativa atualizada
import json
import os
import GPUtil
import psutil
from . import menu  # Mudança para importação relativa
from kivy.uix.widget import Widget 

window_state_before_maximize = {'width': 1280, 'height': 720, 'left': 100, 'top': 100}
previous_window_state = None

def create_main_layout():
    """ Cria o layout principal da aplicação, centralizado na tela. """
    load_window_settings()  # Carregue as configurações da janela primeiro
    main_layout = MainLayout()
    return main_layout
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'  # Mantém a orientação horizontal

        # Espaçadores para ajudar na centralização do botão
        spacer_left = Widget(size_hint_x=1)
        spacer_right = Widget(size_hint_x=1)

        button = CenteredButton(
            text='Hello, Senhor Fox',
            size_hint=(None, None),  # Tamanho fixo
            size=(200, 40),
            pos_hint={'center_x': 0.5}  # Centraliza o botão horizontalmente
        )

        # Adiciona os espaçadores e o botão ao layout
        self.add_widget(spacer_left)
        self.add_widget(button)
        self.add_widget(spacer_right)

        menu.show_menu()

def load_window_settings():
    """ Carrega as configurações da janela do arquivo JSON. """
    if os.path.exists('window_settings.json'):
        with open('window_settings.json', 'r') as file:
            settings = json.load(file)
            window_settings = settings.get('window', {})
            Window.size = (window_settings.get('width', 1280), window_settings.get('height', 720))
            Window.left = window_settings.get('left', 100)
            Window.top = window_settings.get('top', 100)
    else:
        Window.size = (1280, 720)
        center_window_on_screen()

def save_window_settings():
    """ Salva as configurações da janela e informações do sistema no arquivo JSON. """
    settings = {
        'window': {
            'width': Window.width,
            'height': Window.height,
            'left': Window.left,
            'top': Window.top
        },
        'system': get_system_info()
    }
    with open('window_settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

def on_window_resize_move(instance, width, height):
    """ Salva as configurações quando a janela é redimensionada ou movida. """
    global previous_window_state
    previous_window_state = {'width': width, 'height': height, 'left': Window.left, 'top': Window.top}
    save_window_settings()

def on_maximize(instance):
    """ Armazena o estado da janela antes de maximizar. """
    global previous_window_state
    previous_window_state = {'width': Window.width, 'height': Window.height, 'left': Window.left, 'top': Window.top}

def on_restore(instance):
    """ Restaura o estado da janela ao seu tamanho e posição anteriores após sair do modo maximizado. """
    global previous_window_state
    if previous_window_state:
        Window.size = (previous_window_state['width'], previous_window_state['height'])
        Window.left = previous_window_state['left']
        Window.top = previous_window_state['top']

def center_window_on_screen():
    """ Centraliza a janela na tela. """
    Window.left = (Window.system_size[0] - Window.width) // 2
    Window.top = (Window.system_size[1] - Window.height) // 2

def get_system_info():
    """ Coleta informações do sistema, como GPU e memória. """
    gpus = GPUtil.getGPUs()
    gpu_info = [gpu.name for gpu in gpus]
    memory_info = psutil.virtual_memory().total / (1024 ** 3) # Convertendo para GB
    return {'gpu': gpu_info, 'memory_GB': memory_info}

if __name__ == '__main__':
    load_window_settings()
    MyApp().run()