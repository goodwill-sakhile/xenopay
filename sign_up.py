from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import *
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from touch import TouchBox
ui = Builder.load_string("""
<SignUpScreen>:
	name:"sign_up_screen"
	MDBoxLayout:
		orientation:"vertical"
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		MDBoxLayout:
			size_hint_y:None
			height:"80dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				orientation:"vertical"
				Widget:
				MDIconButton:
					icon:"arrow-left-thick"
					size_hint:None, None
					size:"50dp", "50dp"
					pos_hint:{"center_x":.5, "center_y":.5}
					icon_size:"25dp"
					on_press:root.goBackToLoginScreen()
				Widget:
			MDLabel:
				text:"Xenopay (Signup)"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"18dp"
				color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			FloatLayout:
				size_hint:None, None
				size:self.parent.size
				pos:self.parent.pos
				MDBoxLayout:
					pos:self.parent.pos
					Widget:
					MDBoxLayout:
						size_hint_x:None
						width:"300dp"
						orientation:"vertical"
						spacing:10
						Widget:
						MDTextField:
							hint_text_field:"First Name"
							mode:"rectangle"
							id:first_name_object
							icon_left:"email-variant"
						MDTextField:
							hint_text_field:"Last Name (Surname)"
							mode:"rectangle"
							id:first_name_object
							icon_left:"email-variant"
						MDTextField:
							hint_text_field:"Email@Address"
							mode:"rectangle"
							id:first_name_object
							icon_left:"email-variant"
						MDTextField:
							hint_text_field:"Password"
							mode:"rectangle"
							id:first_name_object
							icon_left:"email-variant"
						MDTextField:
							hint_text_field:"Verify Password"
							mode:"rectangle"
							id:first_name_object
							icon_left:"email-variant"
						MDBoxLayout:
							size_hint_y:None
							height:"40dp"
							LoginBySignUp:
								size_hint_y:None
								height:"30dp"
								radius:[30, 30, 30, 30]
								md_bg_color:0, 154/float(255), 220/float(255), 1
								MDLabel:
									text:"Finish Sign Up"
									text_size:self.size
									halign:"center"
									valign:"middle"
									color:1, 1, 1, 1
						Widget:
					Widget:
""")
class LoginBySignUp(TouchBox):
	def respondToTouch(self):
		pass
class SignUpScreen(MDScreen):
	def goBackToLoginScreen(self):
		self.parent.transition = SlideTransition(direction = "right")
		self.parent.current = "login_screen"