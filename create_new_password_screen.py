from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<CreateNewPasswordScreen>:
	name:"create_new_pasword_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"50dp"
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"arrow-left-top"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					icon_size:"30dp"
				Widget:
			Widget:
		MDBoxLayout:
			#orientation:"vertical"
			Widget:
			MDBoxLayout:
				orientation:"vertical"
				size_hint_x:None
				width:"300dp"
				spacing:10
				MDTextField:
					icon_right:"form-textbox-password"
					hint_text:"New Password"
					icon_right_color_normal:"green"
					pos_hint:{"center_x":.5, "center_y":.5}
					icon_right_color_normal:"white"
                	line_color_normal:"red"
                	hint_text_color_normal:"red"
				MDTextField:
					icon_right:"form-textbox-password"
					hint_text:"Verify Password"
					icon_right_color_normal:"green"
					pos_hint:{"center_x":.5, "center_y":.5}
					icon_right_color_normal:"white"
                	line_color_normal:"red"
                	hint_text_color_normal:"red"
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					md_bg_color:0, 0, 0, 1
					radius:[20, 20, 20, 20]
					MDLabel:
						text:"Change Password"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
			Widget:
		Widget:
""")
class CreateNewPasswordScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = CreateNewPasswordScreen()
		return root
if __name__ == "__main__":
	TestApp().run()