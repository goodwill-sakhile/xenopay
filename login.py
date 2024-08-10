from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<LoginScreen>:
	name:"login_screen"
	id:login_screen_object
	FloatLayout:
		pos:self.parent.pos
		size:self.parent.size
		MDBoxLayout:
			orientation:"vertical"
			pos:self.parent.pos
			Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				Widget:
				MDTextField:
					#root:login_screen
					id:email_login_object
					size_hint_x:None
					width:"300dp"
					hint_text:"Email"
					helper_text: "address@gmail.com"
					validator:"email"
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				Widget:
				MDTextField:
					id:password_login_object
					size_hint_x:None
					width:"300dp"
					hint_text:"Password"
					helper_text:"*********"
					password:True
					validator:"email"
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"40dp"
				Widget:
				LoginButtonBox:
					root:login_screen_object
					radius:[30, 30, 30, 30]
					size_hint:None, None
					width:"300dp"
					height:"30dp"
					md_bg_color:[0, 156/float(255), 255/float(255), 1]
					MDLabel:
						text:"Login"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				Widget:
				MDIconButton:
					icon:"refresh"
					size_hint:None, None
					size:"50dp", "50dp"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:[0, 0, 0, 1]
				Widget:
			Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				padding:"10dp"
				Widget:
				SignUpBox:
					root:login_screen_object
					size_hint:None, None
					size:"300dp", "30dp"
					md_bg_color:0, 0, 0, 1
					radius:[30, 30, 30, 30]
					MDLabel:
						text:"Sign-Up"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				Widget:
		MDBoxLayout:
			pos:self.parent.pos
			ScreenManager:
				#MDScreen:
					#name:"empty_screen"
				MDScreen:
					name:"popups_screen"
					MDBoxLayout:
						orientation:"vertical"
""")
class LoginScreen(MDScreen):
	pass
class SignUpBox(TouchBox):
    def respondToTouch(self):
        print("Respond to touch")
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "sign_up_screen"
class LoginButtonBox(TouchBox):
    def responseForEmptyTextBox(self):
    	pass
    def respondToTouch(self):
        email = self.root.ids.email_login_object.text
        password = self.root.ids.password_login_object.text
        print(email, password)
class AppTest(MDApp):
	def build(self):
		root = LoginScreen()
		return root
if __name__ == "__main__":
	AppTest().run()