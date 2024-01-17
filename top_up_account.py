from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
root = Builder.load_string("""
<TopUpAccountScreen>:
	name:"top_up_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			MDBoxLayout:
				size_hint:None, None
				size:"50dp", "100dp"
				orientation:"vertical"
				Widget:
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"arrow-left-top"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
					on_press:self.goBackHome()
				Widget:
			MDBoxLayout:
				MDLabel:
					text:"Account Top Up"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:1, 1, 1, 1
					font_size:"25dp"
			MDBoxLayout:
				size_hint_x:None
				widtg:"50dp"
		MDBoxLayout:
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				Widget:
				MDTextField:
					icon_left:"cash"
					hint_text:"AMOUNT"
					mode:"rectangle"
					line_color_normal:0, 154/float(255), 255/float(255),  1
				MDTextField:
					icon_left:"card"
					hint_text:"CARD NUMBER"
					mode:"rectangle"
					line_color_normal:0, 154/float(255), 255/float(255),  1
				MDBoxLayout:
					size_hint_y:None
					height:"70dp"
					MDTextField:
						icon_left:"clock-time-nine"
						hint_text:"EXPIRY DATE"
						mode:"rectangle"
						line_color_normal:0, 154/float(255), 255/float(255),  1
					Widget:
						size_hint_x:None
						width:"40dp"
					MDTextField:
						icon_left:"numeric"
						hint_text:"CVV"
						mode:"rectangle"
						line_color_normal:0, 154/float(255), 255/float(255),  1
				MDBoxLayout:
					size_hint_y:None
					height:"70dp"
					MDTextField:
						icon_left:"account-card"
						hint_text:"INITIALS & SURNAME"
						mode:"rectangle"
						line_color_normal:0, 154/float(255), 255/float(255),  1
				MDBoxLayout:
					size_hint_y:None
					height:"60dp"
					padding:"0dp", "15dp"
					MDBoxLayout:
						radius:[30, 30, 30, 30]
						md_bg_color:0, 0/float(255), 0/float(255), 1
						MDLabel:
							text:"Top Up"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				Widget:
			Widget:
""")
class TopUpAccountScreen(MDScreen):
	def goBackHome(self):
		self.parent.transition = SlideTransition(direction = "right")
		self.parent.current = "home_screen"
class TestApp(MDApp):
	def build(self):
		root = ScreenManager()
		top_up = TopUpAccountScreen()
		root.add_widget(top_up)
		return root
if __name__ == "__main__":
	TestApp().run() 