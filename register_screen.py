import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<SubScreenOneForwardButton>
    size_hint_y:None
    height:"40dp"
    md_bg_color:0, 0, 0, 1
    radius:20, 20, 20, 20
<RegisterScreen>:
    name:"register_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
        MDBoxLayout:
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:5
            SubScreenOneForwardButton
""")
class RegisterScreen(MDScreen):
    pass
class RegisterTestApp(MDApp):
    def build(self):
        root = RegisterScreen()
        return root
if __name__ == "__main__":
    RegisterTestApp().run()
