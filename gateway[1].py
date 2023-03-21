from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from login import LoginScreen
from signup import SignUpScreen
from kivymd.app import MDApp
ui = Builder.load_string("""
<GatewayScreen>:
    name:"gateway_screen"
    id:gate_way_screen
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            ScreenManager:
                id:gateway_sub_screen_manager
                root:gate_way_screen
                LoginScreen:
                SignUpScreen:
""")
class GatewayScreen(MDScreen):
    pass
class Te(MDApp):
    def build(self):
        root = GatewayScreen()
        return root
if __name__ == "__main__":
    Te().run()