from kivy.app import App
from Module import layout, config  # Certifique-se de que 'config' está sendo importado

class MyApp(App):
    def build(self):
        return layout.create_main_layout()

    def on_stop(self):
        # Chamada corrigida para a função 'save_window_settings' no módulo 'config'
        config.save_window_settings()

if __name__ == '__main__':
    MyApp().run()
