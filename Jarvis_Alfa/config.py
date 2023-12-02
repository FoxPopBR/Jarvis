import json
import os
from kivy.core.window import Window
import GPUtil
import psutil

class WindowManager:
    @staticmethod
    def load_window_settings(config_file):
        """Carrega as configurações da janela do arquivo JSON."""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as file:
                    settings = json.load(file)
                    previous_window_state = settings.get('window', {})
                    Window.size = (
                        previous_window_state.get('width', 1280),
                        previous_window_state.get('height', 720)
                    )
                    Window.left = previous_window_state.get('left', 100)
                    Window.top = previous_window_state.get('top', 100)

        except Exception as e:
            print(f"Erro ao carregar configurações da janela: {e}")

    @staticmethod
    def save_window_settings(config_file):
        """Salva as configurações da janela e informações do sistema no arquivo JSON."""
        try:
            settings = {
                'window': {
                    'width': Window.width,
                    'height': Window.height,
                    'left': Window.left,
                    'top': Window.top
                }
                # Adicione outras configurações conforme necessário
            }
            with open(config_file, 'w') as file:
                json.dump(settings, file, indent=4)

        except Exception as e:
            print(f"Erro ao salvar configurações da janela: {e}")

class SystemManager:
    @staticmethod
    def get_system_info():
        """Coleta informações do sistema, como GPU e memória."""
        try:
            gpus = GPUtil.getGPUs()
            gpu_info = [gpu.name for gpu in gpus]
            memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Convertendo para GB
            return {'gpu': gpu_info, 'memory_GB': memory_info}

        except Exception as e:
            print(f"Erro ao obter informações do sistema: {e}")

class WidgetManager:
    @staticmethod
    def save_widget_positions(widget_positions, widget_id, x, y):
        """Salva a posição de um widget no dicionário de posições de widgets."""
        widget_positions[widget_id] = {'x': x, 'y': y}

    @staticmethod
    def load_widget_positions(widget_positions, widget_id):
        """Carrega a posição de um widget do dicionário de posições de widgets."""
        return widget_positions.get(widget_id, {'x': 0, 'y': 0})  # Retorna (0, 0) se não encontrar a posição
