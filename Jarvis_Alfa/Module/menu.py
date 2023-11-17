from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.core.window import Window
from .widgets import CenteredButton  # Importação relativa atualizada
from kivy.clock import Clock

def show_menu():
    def update_menu_position(dt):
        menu_layout.center = Window.center

    start_button = CenteredButton(text='Iniciar', size_hint=(None, None), height=40, width=200)
    config_button = CenteredButton(text='Configurações', size_hint=(None, None), height=40, width=200)
    exit_button = CenteredButton(text='Sair', size_hint=(None, None), height=40, width=200)

    # Centralize os textos dos botões horizontalmente
    start_button.text_size = (start_button.width, None)
    config_button.text_size = (config_button.width, None)
    exit_button.text_size = (exit_button.width, None)

    menu_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
    menu_layout.size = (200, 200)
    menu_layout.center = Window.center  # Centralize o layout do menu no início

    menu_layout.add_widget(start_button)
    menu_layout.add_widget(config_button)
    menu_layout.add_widget(exit_button)

    start_button.bind(on_press=lambda x: menu_popup.dismiss())
    config_button.bind(on_press=lambda x: show_config_menu())
    exit_button.bind(on_press=lambda x: App.get_running_app().stop())

    menu_popup = Popup(title='Menu Principal', content=menu_layout, size_hint=(None, None), size=(220, 200), auto_dismiss=False)

    # Use o Clock para centralizar o menu no início
    Clock.schedule_once(update_menu_position, 0)

    menu_popup.open()

def show_config_menu():
    config_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
    config_layout.size = (200, 150)
    
    def update_config_menu_position(dt):
        config_layout.center = Window.center
    
    Clock.schedule_once(update_config_menu_position, 0)  # Chamamos a função após o layout do menu ser criado

    back_button = CenteredButton(text='Voltar', size_hint=(None, None), height=40, width=200)
    config_layout.add_widget(back_button)

    config_popup = Popup(title='Configurações', content=config_layout, size_hint=(None, None), size=(220, 150), auto_dismiss=False)
    back_button.bind(on_press=lambda x: config_popup.dismiss())
    config_popup.open()
