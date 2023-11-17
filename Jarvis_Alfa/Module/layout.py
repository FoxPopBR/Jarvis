from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from .widgets import CenteredButton
import os
import GPUtil
import psutil
from . import menu
from kivy.uix.widget import Widget
from kivy.clock import Clock
from .config import load_window_settings, save_window_settings

window_state_before_maximize = {'width': 1280, 'height': 720, 'left': 100, 'top': 100}
previous_window_state = None

def create_main_layout():
    """ Cria o layout principal da aplicação, centralizado na tela. """
    load_window_settings()
    main_layout = MainLayout()
    Clock.schedule_once(lambda dt: menu.show_menu(), 0.1)
    return main_layout

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        spacer_left = Widget(size_hint_x=1)
        spacer_right = Widget(size_hint_x=1)

        button = CenteredButton(
            text='Hello, Senhor Fox',
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5}
        )

        self.add_widget(spacer_left)
        self.add_widget(button)
        self.add_widget(spacer_right)

def center_window_on_screen():
    """ Centraliza a janela na tela. """
    Window.left = (Window.system_size[0] - Window.width) // 2
    Window.top = (Window.system_size[1] - Window.height) // 2

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

def get_system_info():
    """ Coleta informações do sistema, como GPU e memória. """
    gpus = GPUtil.getGPUs()
    gpu_info = [gpu.name for gpu in gpus]
    memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Convertendo para GB
    return {'gpu': gpu_info, 'memory_GB': memory_info}
