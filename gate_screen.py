from kivymd.uix.screen import MDScreen
from login import LoginScreen
from sign_up_screen import SignUpScreen
from recovery_password_screen import RecoverPasswordScreen
from kivy.lang import Builder
root = Builder.load_string("""
<GateScreen>:
    orientation:"vertical"
    md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
    MDBoxLayout:
        size_hint_y:None
        height:"100dp"
    MDBoxLayout:
        ScreenManager:
            name:"gate_screen"
            LoginScreen:
            SignUpScreen:
            RecoverPasswordScreen:
""")
class GateScreen(MDScreen):
    pass
