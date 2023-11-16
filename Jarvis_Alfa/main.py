from kivy.app import App
from Module import layout

class MyApp(App):
    def build(self):
        return layout.create_main_layout()

    def on_stop(self):
        layout.save_window_settings()

if __name__ == '__main__':
    MyApp().run()
