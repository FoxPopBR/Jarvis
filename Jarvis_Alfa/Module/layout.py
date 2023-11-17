from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from .widgets import CenteredButton
from . import menu
from kivy.uix.widget import Widget
from kivy.clock import Clock
from .config import load_window_settings

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
