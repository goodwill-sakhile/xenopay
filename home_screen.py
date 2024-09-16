from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import *
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from touch import TouchBox
ui = Builder.load_string("""
<BarBox>:
	icon:""
	size_hint:None, None
	size:"140dp", "140dp"
	md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
	radius:10, 10, 10, 10
	Widget:
	MDIconButton:
		icon:root.icon
		size_hint:None, None
		size:"60dp", "60dp"
		icon_size:"40dp"
		theme_text_color:"Custom"
		text_color:1, 1, 1, 1
		pos_hint:{"center_x":.5, "center_y":.5}
	Widget:
<HomeScreen>:
	id:home_screen_object
	name:"home_screen"
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
					icon:"logout-variant"
					size_hint:None, None
					size:"50dp", "50dp"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
				Widget:
			MDLabel:
				text:"Xenopay"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"23dp"
				color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			FloatLayout:
				pos:self.parent.pos
				size_hint:None, None
				size:self.parent.size
				MDBoxLayout:
					pos:self.parent.pos
					Widget:
					MDBoxLayout:
						size_hint_x:None
						width:"300dp"
						orientation:"vertical"
						Widget:
						MDBoxLayout:
							#md_bg_color:0, 0, 1, 1
							MDGridLayout:
								root:home_screen_object
								spacing:10
								cols:2
								roas:2
								WalletBarBox:
									icon:"wallet-plus"
								MoneyTransferBarBox:
									icon:"cash-fast"
								BarBox:
									icon:"bank-transfer"
								BarBox:
									icon:"cog-transfer"
						Widget:
					Widget:
				MDBoxLayout:
					pos:self.parent.pos
					ScreenManager:
						MDScreen:
							name:"empty_screen"
						MDScreen:
							name:"top_pop_box_layer"
""")
class BarBox(TouchBox):
	pass
class WalletBarBox(BarBox):
	def respondToTouch(self):
		self.parent.root.parent.transition  = SlideTransition(direction = "left")
		self.parent.root.parent.current = "wallet_screen"
class MoneyTransferBarBox(BarBox):
	pass
class HomeScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = HomeScreen()
		return root
if __name__ == "__main__":
	TestApp().run()