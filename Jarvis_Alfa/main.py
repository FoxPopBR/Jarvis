from kivy.app import App
from Module import layout

class MyApp(App):
    def build(self):
        layout.load_window_settings()  # Carregar as configurações da janela primeiro
        return layout.create_main_layout()

    def on_stop(self):
        layout.save_window_settings()

if __name__ == '__main__':
    MyApp().run()
