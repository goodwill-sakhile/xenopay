from kivymd.app import MDApp 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<SettingsScreen>:
	name:"settings_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				orientation:"vertical"
				Widget:
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"arrow-left-top"
					theme_text_color:"Custom"
					icon_size:"30dp"
					text_color:[1, 1, 1, 1]
		MDBoxLayout:
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				spacing:20
				MDBoxLayout:
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					radius:20, 20, 20, 20
					md_bg_color:0, 0/float(255), 0/float(255), 1
					MDLabel:
						text:"Change Password"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					radius:20, 20, 20, 20
					md_bg_color:0, 0/float(255), 0/float(255), 1
					MDLabel:
						text:"About"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				MDBoxLayout:
			Widget:
		
""")
class SettingsScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = SettingsScreen()
		return root
if __name__ == "__main__":
	TestApp().run()