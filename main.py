from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from gate_screen import GateScreen
from kivy.lang import Builder
from kivy.core.window import Window
from home_screen import HomeScreen
Window.size = (350, 600)
root = Builder.load_string("""
<MainBox>:
    ScreenManager:
        name:"main_screen"
        HomeScreen:
        GateScreen:
""")
class MainBox(MDBoxLayout):
    pass
class TestApp(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    TestApp().run()
