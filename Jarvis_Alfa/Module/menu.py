from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.core.window import Window
from .widgets import CenteredButton  # Importação relativa
from kivy.clock import Clock

def show_menu():
    def update_menu_position(dt):
        # Esta função ajusta a posição do menu para centralizá-lo na janela
        menu_layout.center = Window.center

    # Criação dos botões com o Centro Button personalizado
    start_button = CenteredButton(text='Iniciar', size_hint=(None, None), height=40, width=200)
    config_button = CenteredButton(text='Configurações', size_hint=(None, None), height=40, width=200)
    exit_button = CenteredButton(text='Sair', size_hint=(None, None), height=40, width=200)

    # Centraliza o texto dos botões
    start_button.text_size = (start_button.width, None)
    config_button.text_size = (config_button.width, None)
    exit_button.text_size = (exit_button.width, None)

    # Criação do layout do menu
    menu_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
    menu_layout.size = (200, 200)

    # Adiciona os botões ao layout do menu
    menu_layout.add_widget(start_button)
    menu_layout.add_widget(config_button)
    menu_layout.add_widget(exit_button)

    # Associação de eventos aos botões
    start_button.bind(on_press=lambda x: menu_popup.dismiss())
    config_button.bind(on_press=lambda x: show_config_menu())
    exit_button.bind(on_press=lambda x: App.get_running_app().stop())

    # Criação do popup do menu principal
    menu_popup = Popup(title='Menu Principal', content=menu_layout, size_hint=(None, None), size=(220, 200), auto_dismiss=False)

    # Agenda a função de atualização da posição do menu para depois que a janela for desenhada
    Clock.schedule_once(update_menu_position, 0)

    # Exibe o popup do menu
    menu_popup.open()

def show_config_menu():
    # Esta função é similar à anterior, mas para o menu de configurações
    config_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
    config_layout.size = (200, 150)
    
    def update_config_menu_position(dt):
        config_layout.center = Window.center

    # Agendamento para centralizar o layout de configurações
    Clock.schedule_once(update_config_menu_position, 0)

    # Botão de volta no menu de configurações
    back_button = CenteredButton(text='Voltar', size_hint=(None, None), height=40, width=200)
    config_layout.add_widget(back_button)

    # Criação do popup de configurações
    config_popup = Popup(title='Configurações', content=config_layout, size_hint=(None, None), size=(220, 150), auto_dismiss=False)
    back_button.bind(on_press=lambda x: config_popup.dismiss())
    config_popup.open()
