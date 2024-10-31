import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from halaman.welcome import WelcomeScreen
from halaman.login import LoginScreen
from halaman.register import RegisterScreen
from halaman.forgotpassword import ForgotpasswordScreen
from halaman.creatanewpassword import CreatanewpasswordScreen
from halaman.passwordchange import PasswordchangeScreen
from halaman.homepage import HomepageScreen
from halaman.manager import ManagerScreen
from kivy.lang import Builder
from kivy.core.window import Window

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        Window.size = (300,610)
        Window.clearcolor = (1, 1, 1, 1)
        kv_path = os.path.join(os.path.dirname(__file__), 'kv')
        Builder.load_file(os.path.join(kv_path, 'welcome.kv'))
        Builder.load_file(os.path.join(kv_path, 'login.kv'))
        Builder.load_file(os.path.join(kv_path, 'register.kv'))
        Builder.load_file(os.path.join(kv_path, 'forgotpassword.kv'))
        Builder.load_file(os.path.join(kv_path, 'creatanewpassword.kv'))
        Builder.load_file(os.path.join(kv_path, 'passwordchange.kv'))
        Builder.load_file(os.path.join(kv_path, 'homepage.kv'))
        Builder.load_file(os.path.join(kv_path, 'manager.kv'))



        sm = MyScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ForgotpasswordScreen(name='forgotpassword'))
        sm.add_widget(CreatanewpasswordScreen(name='creatanewpassword'))
        sm.add_widget(PasswordchangeScreen(name='passwordchange'))
        sm.add_widget(HomepageScreen(name='homepage'))
        sm.add_widget(ManagerScreen(name='manager'))
        sm.current = 'homepage'
        return sm

if __name__ == '__main__':
    MyApp().run()