import json
import os
from kivy.core.window import Window
import GPUtil
import psutil

# Variáveis globais para armazenar o estado anterior da janela
window_state_before_maximize = {'width': 1280, 'height': 720, 'left': 100, 'top': 100}
previous_window_state = None

def load_window_settings():
    """ Carrega as configurações da janela do arquivo JSON. """
    global previous_window_state
    if os.path.exists('window_settings.json'):
        with open('window_settings.json', 'r') as file:
            settings = json.load(file)
            previous_window_state = settings.get('window', {})
            Window.size = (previous_window_state.get('width', 1280), previous_window_state.get('height', 720))
            Window.left = previous_window_state.get('left', 100)
            Window.top = previous_window_state.get('top', 100)
    else:
        Window.size = (1280, 720)
        center_window_on_screen()

def center_window_on_screen():
    """ Centraliza a janela na tela. """
    Window.left = (Window.system_size[0] - Window.width) // 2
    Window.top = (Window.system_size[1] - Window.height) // 2

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

def get_system_info():
    """ Coleta informações do sistema, como GPU e memória. """
    gpus = GPUtil.getGPUs()
    gpu_info = [gpu.name for gpu in gpus]
    memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Convertendo para GB
    return {'gpu': gpu_info, 'memory_GB': memory_info}
