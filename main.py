from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from login import LoginScreen
root = Builder.load_string("""
<MainScreen>:
	name:"main_screen"
	MDBoxLayout:
		ScreenManager:
			LoginScreen:
""")
class MainScreen(MDScreen):
	pass
class XenopayApp(MDApp):
	def build(self):
		root = MainScreen()
		return root
if __name__ == "__main__":
	XenopayApp().run()