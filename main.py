from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from gateway import GatewayScreen
from home_screen import HomeScreen
from kivy.lang import Builder
#from kivy.core.window import Window
#Window.size = (350, 600)
root = Builder.load_string("""
<MainBox>:
    orientation:"vertical"
    MDBoxLayout:
        ScreenManager:
            HomeScreen:
            GatewayScreen:
""")
class MainBox(MDBoxLayout):
    pass
class TestApp(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    TestApp().run()
