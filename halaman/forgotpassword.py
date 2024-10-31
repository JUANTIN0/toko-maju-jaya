from kivy.uix.screenmanager import Screen

class ForgotpasswordScreen(Screen):
    pass

        #layout = BoxLayout(orientation='vertical', padding=[20, 40], spacing=10, size_hint=(1, 1))

        # Back button
        #back_button = Button(text='<', size_hint=(None, None), size=(40, 40), pos_hint={"x": 0, "top": 1})
        #back_button.bind(on_press=self.go_back)
        #layout.add_widget(back_button)

        # Title
        #title = Label(
            #text='Forgot Password?',
            #font_size='24sp',
            #color=(0, 0, 0.5, 1),
            #size_hint=(1, 0.1),
            #pos_hint={'x': 0},
            #halign='left',
            #valign='top',
        #)
        #title.bind(size=title.setter('text_size'))
        #layout.add_widget(title)

        # Description
        #description = Label(
            #text="Don't worry! It occurs. Please enter the email address linked with your account.",
            #font_size='16sp',
            #color=(0.5, 0.5, 0.5, 1),
            #size_hint=(1, 0.8),
            #pos_hint={'x': 0},
            #halign='left',
            #valign='top',
        #)
        #description.bind(size=description.setter('text_size'))
        #layout.add_widget(description)

        # Email input
        #self.email_input = TextInput(
            #hint_text='Enter your email',
            #multiline=False,
            #size_hint=(0.8, None),
            #height=56,
            #padding_y=(10, 10),
            #pos_hint={'top_x': 0.5},
            #halign='center'
        #)
        #layout.add_widget(self.email_input)

        # Send Code button
        #send_code_button = Button(
            #text='Send Code',
            #size_hint=(1, None),
            #height=50,
            #background_color=(0, 0, 0, 1),
            #color=(1, 1, 1, 1)
        #)
        #send_code_button.bind(on_press=self.send_code)
        #layout.add_widget(send_code_button)

        # Remember Password layout
        #remember_password_layout = BoxLayout(
            #orientation='horizontal',
            #size_hint=(1, None),
            #height=40,
            #padding=[10, 10]
        #)
        #remember_password_label = Label(
            #text='Remember Password?',
            #font_size='14sp',
            #color=(0.5, 0.5, 0.5, 1),
            #size_hint=(0.6, 1),
            #halign='right'
        #)
        #login_button = Button(
            #text='Login',
            #size_hint=(0.4, 1),
            #background_color=(0, 0, 0, 0),
            #color=(0, 0.5, 1, 1)
        #)
        #login_button.bind(on_press=self.login)

        #remember_password_layout.add_widget(remember_password_label)
        #remember_password_layout.add_widget(login_button)
        #layout.add_widget(remember_password_layout)

        #self.add_widget(layout)

    #def go_back(self, instance):
        # Implement the back button functionality
        #pass

    #def send_code(self, instance):
        # Implement the send code functionality
        #pass

    #ef login(self, instance):
        # Implement the login functionality
        #pass


#class MyApp(App):
    #def build(self):
        # Set background color to white
        #Window.clearcolor = (1, 1, 1, 1)  # White (R, G, B, A)

        #sm = ScreenManager()
        #sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        #return sm


#if __name__ == '__main__':
    #MyApp().run()
