from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from new_login import LoginScreen
from sign_up import SignUpScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<MainBox>:
	MDBoxLayout:
		ScreenManager:
			LoginScreen:
			SignUpScreen:
			
""")
class MainBox(MDBoxLayout):
	pass
class XenopayApp(MDApp):
	def build(self):
		root = MainBox()
		return root
		#root = MainScreenManager()
		#return root
if __name__ == "__main__":
	XenopayApp().run()