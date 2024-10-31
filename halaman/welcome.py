from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    pass

# class MainApp(App):
#     def build(self):
#         # Set background color to light grey
#         Window.clearcolor = (0.9, 0.9, 0.9, 1)
        
#         # Manually set the window size if needed
#         Window.size = (300, 600)

#         # Load the KV file
#         kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'welcomescreen.kv')
#         Builder.load_file(kv_path)

#         # Create ScreenManager
#         sm = ScreenManager()
        
#         # Add screens to the ScreenManager
#         sm.add_widget(WelcomeScreen(name='login'))

#         return sm

# if __name__ == '__main__':
#     MainApp().run()
