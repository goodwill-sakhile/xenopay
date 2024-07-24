from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from touch import TouchBox
root = Builder.load_string("""
<LoginButton>:
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
<SignUpScreenButton>:
	size_hint_y:None
	height:"30dp"
	radius:30, 30, 30, 30
	md_bg_color:0, 0/float(255), 0/float(255), 1
	MDLabel:
		text:"Sign Up"
		text_size:self.size
		halign:"center"
		valign:"middle"
		color:1, 1, 1, 1
<LoginScreen>:
	id:login_screen_object
	name:"login_screen"
	MDBoxLayout:
		md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"80dp"
			md_bg_color:0, 0, 0, 1
			padding:"15dp", "0dp", "0dp", "0dp"
			MDLabel:
				text:"Xenopay"
				text_size:self.size
				halign:"left"
				valign:"middle"
				font_size:"25dp"
				color:1, 1, 1, 1
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
						spacing:15
						Widget:
						MDTextField:
							id:email_text_field
							text:""
							hint_text:"Email"
							helper_text:"user@email.com"
							validator:"email"
						MDTextField:
							id:password_text_field
							text:""
							hint_text:"Password"
							helper_text:"********"
							validator:"email"
						LoginButton:
							root:login_screen_object
						Widget:
						MDBoxLayout:
							size_hint_y:None
							height:"50dp"
							padding:"0dp", "15dp"
							Widget:
							MDBoxLayout:
								size_hint_x:None
								width:"310dp"
								SignUpScreenButton:
							Widget:
					Widget:
				MDBoxLayout:
					pos:self.parent.pos
					ScreenManager:
						
						MDScreen:
							name:"dialog_screen"
							MDBoxLayout:
								Widget:
								MDBoxLayout:
									size_hint_x:None
									width:"300dp"
									orientation:"vertical"
									Widget:
									MDBoxLayout:
										md_bg_color:0, 0, 0, 1
										size_hint_y:None
										height:"400dp"
									Widget:
								Widget:
						MDScreen:
							name:"empty_screen"
""")
class LoginButton(TouchBox):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def getLoginCredentials(self):
		email  = self.root.ids.email_text_field.text
		password = self.root.ids.password_text_field.text
		print("Email: ", email)
		print("Password: ", password)
	def respondToTouch(self):
		self.getLoginCredentials()
class SignUpScreenButton(MDBoxLayout):
	pass
class LoginScreen(MDScreen):
	pass