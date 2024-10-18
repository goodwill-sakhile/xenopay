from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from touch import TouchBox
ui = Builder.load_string("""
<LoginButton>:
    size_hint_y:None
    height:"30dp"
    radius:30, 30, 30, 30
    md_bg_color: 0, 154/float(255), 220/float(255), 1
    MDLabel:
        text:"Login"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
<GoToForgotButton>:
    size_hint_y:None
    height:"30dp"
    radius:30, 30, 30, 30
    md_bg_color:0, 154/float(255), 220/float(255), 1
    MDLabel:
        text:"Forgot Password"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
<GoToSignUpButton>:
    size_hint_y:None
    height:"30dp"
    radius:30, 30, 30, 30
    md_bg_color:0, 0, 0, 1
    MDLabel:
        text:"Sign-Up"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
        bold:True
<LoginScreen>:
    name:"login_screen"
    id:login_screen_object
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:0, 0, 0, 1
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            MDLabel:
                text:"Xenopay"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:1, 1, 1, 1
        MDBoxLaytout:
            radius:[30, 30, 0, 0]
            md_bd_color:47/float(255), 79/float(255), 79/float(255), 1
            FloatLayout:
                size_hint:None, None
                size:self.parent.size
                pos:self.parent.pos
                MDBoxLayout:
                    pos:self.parent.pos
                    Widget:
                    MDBoxLayout:
                        spacing:10
                        size_hint_x:None
                        width:"300dp"
                        orientation:"vertical"
                        Widget:
                        MDTextField:
                            hint_text:"Email@Address"
                            mode:"rectangle"
                            id:email_login_text_object
                            icon_left:"email-variant"
                        MDTextField:
                            hint_text:"********"
                            mode:"rectangle"
                            id:password_login_text_object
                            icon_left:"lock_question"
                        LoginButton:
                            root:login_screen_object
                        GoToForgotButton:
                        Widget:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"50dp"
                            padding:"0dp", "10dp"
                            GoToSignUpButton:
                                root:login_screen_object
                    Widget:
                MDBoxLayout:
                    pos:self.parent.pos
                    ScreenManager:
                        MDScreen:
                            name:"empty_screen"
                        MDScreen:
                            name:"error_screen"
                            MDBoxLayout:
                                Widget:
                                MDBoxLayout:
                                    size_hint_x:None
                                    width:"200dp"
                                    orientation:"vertical"
                                    Widget:
                                    MDBoxLayout:
                                        radius:10, 10, 10, 10
                                        md_bg_color: 0, 0, 0, 1
                                        orientation:"vertical"
                                        size_hint_y:None
                                        height:"300dp"
                                        MDBoxLayout:
                                            MDLabel:
                                                id:error_message
                                                text:""
                                                text_size:self.size
                                                font_name:"18dp"
                                                halign:"center"
                                                valign:"middle"
                                                color:1, 1, 1, 1
                                        MDBoxLayout:
                                            size_hint_y:None
                                            height:"50dp"
                                            padding:"5dp", "10dp"
                                            MDBoxLayout:
                                                size_hint_y:None
                                                height:"30dp"
                                                radius:30, 30, 30, 30
                                                md_bg_color:0, 154/float(255), 220/float(255), 1
                                                MDLabel:
                                                    text:"Ok"
                                                    text_size:self.size
                                                    halign:"center"
                                                    valign:"middle"
                                                    bold:True
                                    Widget:
                                Widget:
""")
class LoginButton(TouchBox):
    def checkEmailValidity(self, email):
        email_valid = False
        if "@" in email:
            email_valid = True
            at_symbol_index = email.index("@")
            if "." in email[at_symbol_index +1:]:
                email_valid = True
            else:
                email_valid = False
        return email_valid
    def checkCharType(self, full_string):
        alpha = 0
        numeric = 0
        mixed = False
        strange = 0
        strange_char = ["!@#$%^&*()-_+={}[]|\.,/?:;~'""`"]
        for i in full_string:
            if i.isalpha():
                alpha += 1
            elif i.isdigit():
                numeric += 1
            elif i in strange_char:
                strange += 1
        if ((alpha > 0) and (strange > 0) and (numeric > 0)):
            mixed = True
        return mixed
    def checkPasswordValidity(self, password):
        password_valid = False
        if len(password) >= 8:
            password_valid = True
            mixed = self.checkCharType(password)
            if mixed:
                password_valid = True
            else:
                password_valid = False
        return password_valid
    def submitLoginDetails(self, email, password):
        credentials_valid = False
        return valid_credentials
    def incorrectCredentialNotifyer(self, email_valid, password_valid):
        if email_valid != True:
            self.ids.error_message.text = "Email Enterd is not valid!"
        elif password_valid != True:
            self.ids.error_message.text = "Non Valid Password \n (Put alpha, digit, strange digit)"
    def respondToTouch(self):
        email = self.root.ids.email_login_text_object.text
        password = self.root.ids.password_login_text_object.text
        email_valid= self.checkEmailValidity(email)
        password_valid = self.checkPassowrdValidity(password)
        if email_valid and password_valid:
            credentials_valid = self.submitLoginDetails(email, password)
            if credentials_valid:
                self.root.parent.transition = SlideTransition(direction = "left")
                self.root.parent.current = "home_screen"
        elif:
            self.incorrectCredentialNotifyer(email_valid, password_valid)
class GoToSignUpButton(TouchBox):
    def respondToTouch(self):
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "sign_up_screen"
class LoginScreen(MDScreen):
    pass
class TestApp(MDApp):
    def build(self):
        root = LoginScreen()
        return root
if __name__ == "__main__":
    TestApp().run()
