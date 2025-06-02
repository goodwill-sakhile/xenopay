import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<GoToSignUpScreenButton>:
    size_hint_y:None
    height:"40dp"
    md_bg_color:0, 0/float(255), 0/float(255), 1
    radius:20, 20, 20, 20
    MDLabel:
        text:"Sign Up"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
<LogintButton>:
    size_hint_y:None
    height:"40dp"
    md_bg_color:0, 154/float(255), 220/float(255), 1
    radius:20, 20, 20, 20
    MDLabel:
        text:"Login"
        text_size:self.size
        halign:"center"
        valign:"middle"
<LoginScreen>:
    name:"login_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
        MDBoxLayout:
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"300dp"
                orientation:"vertical"
                MDTextField:
                    hint_text:"Email@Address.com"
                    icon_left:"email"
                    theme_line_color:"Custom"
                    line_color:0, 0, 0, 1
                    mode:"line"
                MDTextField:
                    hint_text:"********"
                    icon_left:"onepassword"
                    theme_line_color:"Custom"
                    line_color:0, 0, 0, 1
                    mode:"line"
                LogintButton
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:10
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"300dp"
                GoToSignUpScreenButton:
            Widget:
""")
class GoToSignUpScreenButton(MDBoxLayout):
    pass
class LogintButton(MDBoxLayout):
    pass
class LoginScreen(MDScreen):
    pass
class LoginAppTest(MDApp):
    def build(self):
        root = LoginScreen()
        return root
if __name__ == "__main__":
    LoginAppTest().run()
