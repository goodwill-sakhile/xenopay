from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from touch import TouchBox
ui = Builder.load_string("""
<LoginScreen>:
	id:login_screen
	name:"login_screen"
	MDBoxLayout:
		orientation:"vertical"
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		MDBoxLayout:
			size_hint_y:None
			height:"80dp"
			MDLabel:
				text:"Xenopay (Login)"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"18dp"
				color:1, 1, 1, 1
		MDBoxLayout:
			FloatLayout:
				size_hint:None, None
				size:self.parent.size
				#pos_hint:None, None
				pos:self.parent.pos
				MDBoxLayout:
					#pos_hint:None, None
					pos:self.parent.pos
					Widget:
					MDBoxLayout:
						size_hint_x:None
						width:"300dp"
						orientation:"vertical"
						spacing:10
						Widget:
						MDTextField:
							hint_text:"Email@Address"
							mode:"rectangle"
							id:emal_login_text_object
							icon_left:"email-variant"
						MDTextField:
							hint_text:"********"
							mode:"rectangle"
							id:password_login_text_object
							icon_left:"lock-question"
						MDBoxLayout:
							size_hint_y:None
							height:"40dp"
							LoginButtonBox:
								size_hint_y:None
								height:"30dp"
								radius:30, 30, 30, 30
								md_bg_color:0, 154/float(255), 220/float(255), 1
								MDLabel:
									text:"Login"
									text_size:self.size
									halign:"center"
									valign:"middle"
									color:1, 1, 1, 1
						Widget:
						MDBoxLayout:
							size_hint_y:None
							height:"50dp"
							padding:"0dp", "10dp"
							SignUpButtonBox:
								root:login_screen
								size_hint_y:None
								height:"30dp"
								md_bg_color:0, 0, 0, 1
								radius:30, 30, 30, 30
								MDLabel:
									text:"Sign Up"
									text_size:self.size
									halign:"center"
									valign:"middle"
									color:1, 1, 1, 1
					Widget:
""")
class LoginButtonBox(MDBoxLayout):
	pass
class SignUpButtonBox(TouchBox):
	def respondToTouch(self):
		self.root.parent.transition = SlideTransition(direction = "left")
		self.root.parent.current = "sign_up_screen"
		print("Go to Sign Up Screen")
class LoginScreen(MDScreen):
	pass