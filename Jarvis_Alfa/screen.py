from kivy.uix.popup import Popup
from kivy.core.window import Window
from Module.widgets import CustomWidgetFactory
from kivy.clock import Clock
from kivy.app import App  # Adicionei o import do App

class ScreenManager:
    def __init__(self, widget_factory):
        self.widget_factory = widget_factory
        self.show_menu()

    def show_menu(self):
        def update_menu_position(dt):
            self.menu_layout.center = Window.center  # Corrigido o escopo da variável menu_layout

        # Criação dos botões com o Centro Button personalizado
        start_button = self.widget_factory.create_centered_button(text='Iniciar', on_press=self.menu_start_pressed)
        config_button = self.widget_factory.create_centered_button(text='Configurações', on_press=self.menu_config_pressed)
        exit_button = self.widget_factory.create_centered_button(text='Sair', on_press=self.menu_exit_pressed)

        # Criação do layout do menu
        self.menu_layout = self.widget_factory.create_vertical_layout(spacing=10, size_hint=(None, None))
        self.menu_layout.size = (200, 200)

        # Adiciona os botões ao layout do menu
        self.menu_layout.add_widget(start_button)
        self.menu_layout.add_widget(config_button)
        self.menu_layout.add_widget(exit_button)

        # Associação de eventos aos botões

        # Criação do popup do menu principal
        self.menu_popup = Popup(title='Menu Principal', content=self.menu_layout, size_hint=(None, None), size=(220, 200),
                                auto_dismiss=False)

        # Agenda a função de atualização da posição do menu para depois que a janela for desenhada
        Clock.schedule_once(update_menu_position, 0)

        # Exibe o popup do menu
        self.menu_popup.open()

    def show_config_menu(self):
        config_layout = self.widget_factory.create_vertical_layout(spacing=10, size_hint=(None, None))
        config_layout.size = (200, 150)

        def update_config_menu_position(dt):
            config_layout.center = Window.center

        # Agendamento para centralizar o layout de configurações
        Clock.schedule_once(update_config_menu_position, 0)

        # Botão de volta no menu de configurações
        back_button = self.widget_factory.create_centered_button(text='Voltar', on_press=self.config_back_pressed)
        config_layout.add_widget(back_button)

        # Criação do popup de configurações
        config_popup = Popup(title='Configurações', content=config_layout, size_hint=(None, None), size=(220, 150),
                             auto_dismiss=False)
        back_button.bind(on_press=lambda x: config_popup.dismiss())
        config_popup.open()

    def menu_start_pressed(self, instance):
        # Lógica quando o botão 'Iniciar' é pressionado
        print("Iniciar Pressionado")
        self.menu_popup.dismiss()  # Corrigido para usar self.menu_popup

    def menu_config_pressed(self, instance):
        # Lógica quando o botão 'Configurações' é pressionado
        self.show_config_menu()

    def menu_exit_pressed(self, instance):
        # Lógica quando o botão 'Sair' é pressionado
        App.get_running_app().stop()

    def config_back_pressed(self, instance):
        # Lógica quando o botão 'Voltar' no menu de configurações é pressionado
        print("Voltar Pressionado")

# Exemplo de uso:
# widget_factory = CustomWidgetFactory()
# screen_manager = ScreenManager(widget_factory)
