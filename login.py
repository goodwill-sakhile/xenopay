from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.lang import Builder
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
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				spacing:15
				Widget:
				MDTextField:
					hint_text:"Email"
					helper_text:"user@email.com"
					validator:"email"
				MDTextField:
					hint_text:"Password"
					helper_text:"********"
					validator:"email"
				LoginButton:
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
""")
class LoginButton(MDBoxLayout):
	pass
class SignUpScreenButton(MDBoxLayout):
	pass
class LoginScreen(MDScreen):
	pass