from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from login import LoginScreen
from sign_up_screen import SignUpScreen
from recovery_password_screen import RecoverPasswordScreen
#from kivy.core.window import Window
#Window.size = (350, 600)
root = Builder.load_string("""
<GatewayScreen>:
    MDBoxLayout:
    	orientation:"vertical"
	    md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
	    MDBoxLayout:
	        size_hint_y:None
	        height:"100dp"
	        md_bg_color:0, 0, 0, 1
	    MDBoxLayout:
	        ScreenManager:
	            #RecoverPasswordScreen:
	            LoginScreen:
	            SignUpScreen:
""")
class GatewayScreen(MDScreen):
    pass
class TestApp(MDApp):
	def build(self):
		root = GatewayScreen()
		return root
if __name__ == "__main__":
	TestApp().run()
