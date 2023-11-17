import json
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from uuid import uuid4

kivy.require('1.0.9')
# Módulo separado para manipulação de dados do usuário
class UserData:
    @staticmethod
    def save_user_data(username, login_name, password, email):
        data = UserData.load_user_data()
        user_id = str(uuid4())
        data[user_id] = {'nome_de_login': login_name, 'nome_de_usuario': username, 'senha': password, 'email': email}
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_user_data():
        try:
            with open('user.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text='Nome de Login'))
        self.login_name = TextInput(multiline=False)
        self.add_widget(self.login_name)

        self.add_widget(Label(text='Senha'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        btn_layout = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        self.login_btn = Button(text='Entrar', size_hint=(None, None), size=(100, 50))
        self.login_btn.bind(on_press=self.validate_user)
        btn_layout.add_widget(self.login_btn)

        self.new_user_btn = Button(text='Novo', size_hint=(None, None), size=(100, 50))
        self.new_user_btn.bind(on_press=self.open_signup)
        btn_layout.add_widget(self.new_user_btn)

        self.exit_btn = Button(text='Sair', size_hint=(None, None), size=(100, 50))
        self.exit_btn.bind(on_press=self.exit_app)
        btn_layout.add_widget(self.exit_btn)

        self.add_widget(btn_layout)

    def validate_user(self, instance):
        login_name = self.login_name.text
        password = self.password.text
        if not login_name or not password:
            self.show_popup('Por favor, insira o nome de usuário e senha')
            return
        users = UserData.load_user_data()
        user_found = False
        for user in users.values():
            if user['nome_de_login'] == login_name and user['senha'] == password:
                user_found = True
                break
        if user_found:
            # Usuário validado com sucesso
            pass  # Implementar ação após login bem-sucedido
        else:
            self.show_popup('Usuário não cadastrado ou senha incorreta')


    def show_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        close_btn = Button(text='Fechar', size_hint=(None, None), size=(100, 50))
        close_btn.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(close_btn)
        popup = Popup(title='Aviso', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def open_signup(self, instance):
        self.clear_widgets()
        self.add_widget(SignupScreen())

    def exit_app(self, instance):
        App.get_running_app().stop()

class SignupScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text='Nome de Usuário'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Nome de Login'))
        self.login_name = TextInput(multiline=False)
        self.add_widget(self.login_name)

        self.add_widget(Label(text='Senha'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text='E-mail'))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        btn_layout = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        self.signup_btn = Button(text='Cadastrar', size_hint=(None, None), size=(100, 50))
        self.signup_btn.bind(on_press=self.signup_user)
        btn_layout.add_widget(self.signup_btn)

        self.cancel_btn = Button(text='Cancelar', size_hint=(None, None), size=(100, 50))
        self.cancel_btn.bind(on_press=self.cancel_signup)
        btn_layout.add_widget(self.cancel_btn)

        self.add_widget(btn_layout)

    def signup_user(self, instance):
        username = self.username.text
        login_name = self.login_name.text
        password = self.password.text
        email = self.email.text

        if not username or not login_name or not password or not email:
            self.show_popup('Por favor, preencha todos os campos')
            return

        users = UserData.load_user_data()
        if any(user['nome_de_login'] == login_name for user in users.values()):
            self.show_popup('Nome de login já está em uso')
        else:
            UserData.save_user_data(username, login_name, password, email)
            self.show_popup('Usuário cadastrado com sucesso!', self.back_to_login)

    def back_to_login(self):
        self.clear_widgets()
        self.add_widget(LoginScreen())    

    def show_popup(self, message, on_dismiss=None):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        close_btn = Button(text='OK', size_hint=(None, None), size=(100, 50))
        popup = Popup(title='Informação', content=content, size_hint=(None, None), size=(300, 200), auto_dismiss=False)
        close_btn.bind(on_press=lambda x: self.close_popup(popup, on_dismiss))
        content.add_widget(close_btn)
        popup.open()

    def close_popup(self, popup, on_dismiss):
        popup.dismiss()
        if on_dismiss:
            on_dismiss()

    def cancel_signup(self, instance):
        self.clear_widgets()
        self.add_widget(LoginScreen())

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
