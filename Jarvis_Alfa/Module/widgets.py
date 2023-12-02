from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class CustomWidgetFactory:
    @staticmethod
    def create_centered_button(text="", on_press=None, **kwargs):
        """Cria um botão centralizado."""
        button = Button(text=text, on_press=on_press, **kwargs)
        button.bind(size=button.update_text_size)
        button.halign = "center"
        button.valign = "middle"
        return button

    @staticmethod
    def create_label(text="", font_size=15, **kwargs):
        """Cria um rótulo com opções padrão."""
        label = Label(text=text, font_size=font_size, **kwargs)
        return label

    @staticmethod
    def create_horizontal_layout(**kwargs):
        """Cria um layout horizontal."""
        return BoxLayout(orientation="horizontal", **kwargs)

    @staticmethod
    def create_vertical_layout(**kwargs):
        """Cria um layout vertical."""
        return BoxLayout(orientation="vertical", **kwargs)

# Exemplo de uso:
# widget_factory = CustomWidgetFactory()
# centered_button = widget_factory.create_centered_button(text="Clique Aqui", on_press=callback_function)
# label = widget_factory.create_label(text="Texto do Rótulo", font_size=20)
# horizontal_layout = widget_factory.create_horizontal_layout()
# vertical_layout = widget_factory.create_vertical_layout()
