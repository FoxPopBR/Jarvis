from kivy.app import App
from Module.layout import MainLayout, load_window_settings, save_window_settings
from config import load_window_settings, save_window_settings
class MyApp(App):
    def build(self):
        # Carrega as configurações da janela e posições dos widgets
        load_window_settings()

        main_layout = MainLayout.create_main_layout()

        # Adapte esta parte para salvar as posições dos widgets específicos
        # Substitua 'widget_id' pelos identificadores reais dos seus widgets
        main_layout.bind(on_close=lambda instance: self.save_widget_positions('widget_id'))

        return main_layout

    def save_widget_positions(self, widget_id):
        # Adapte para salvar as posições dos widgets conforme a estrutura do seu código
        # Exemplo: save_widget_positions('widget_id', x, y)
        pass

    def on_stop(self):
        # Salva as configurações da janela antes de fechar o aplicativo
        save_window_settings()

if __name__ == '__main__':
    MyApp().run()
 