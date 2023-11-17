from kivy.uix.button import Button

class CenteredButton(Button):
    def __init__(self, **kwargs):
        super(CenteredButton, self).__init__(**kwargs)
        self.bind(size=self.update_text_size)
        self.halign = "center"
        self.valign = "middle"

    def update_text_size(self, *_):
        self.text_size = self.size
