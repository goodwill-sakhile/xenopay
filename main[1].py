from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder
from home import HomeScreen
from gateway import GatewayScreen
from forgot_password import ForgotPasswordScreen
ui = Builder.load_string("""
<MainScreenManager>:
    HomeScreen:
    GatewayScreen:
        id:gate_way_screen
    ForgotPasswordScreen:
""")

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def addGatewayScreen(self, **kwargs):
        time.sleep(2)
        self.transition = SlideTransition(direction = "left")
        self.current = "gateway_screen"
class MainApp(MDApp):
    def build(self):
        #call the top screen manager of the whole app
        return MainScreenManager()
if __name__ == "__main__":
    MainApp().run()