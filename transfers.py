from kivymd.app import MDApp 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<ButtonBox>:
	orientation:"vertical"
	Widget:
	MDBoxLayout:
		Widget:
		MDIconButton:
			id:button
			size_hint:None, None
			size:"40dp", "40dp"
			icon:""
			icon_size:"40dp"
			theme_text_color:"Custom"
			text_color:[1, 1, 1, 1]
		Widget:
	Widget:
<TransferScreen>:
	name:"transfer_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
		MDBoxLayout:
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				spacing:10
				Widget:
				MDBoxLayout:
					ButtonsGrid:
						size_hinth:None, None
						size:"300dp", "300dp"
						cols:3
						rows:4
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					spacing:10
					MDBoxLayout:
						size_hint_y:None
						height:"30dp"
						radius:[30, 30, 30, 30]
						md_bg_color:0, 0, 0, 1
						MDLabel:
							text:"Send"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
							bold:True
					MDBoxLayout:
						size_hint_y:None
						height:"30dp"
						padding:"10dp", "0dp"
						radius:[30, 30, 30, 30]
						md_bg_color:0, 0, 0, 1
						MDLabel:
							text:"Request"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
							bold:True
				Widget:
					size_hint_y:None
					height:"100dp"
			Widget:
""")
class TransferScreen(MDScreen):
	pass
class ButtonBox(MDBoxLayout):
	pass
class ButtonsGrid(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.placeButtons()
	def placeButtons(self):
		for i in range(1,  13):
			button_box = ButtonBox()
			if i == 10:
				button_box.ids.button.icon = "undo-variant"
			elif i == 11:
				button_box.ids.button.icon = "numeric-0-circle"
			elif i == 12:
				button_box.ids.button.icon = "close"
			else:
				button_box.ids.button.icon = "numeric-" + str(i) + "-circle"
			self.add_widget(button_box)
class TestApp(MDApp):
	def build(self):
		root = TransferScreen()
		return root
if __name__ == "__main__":
	TestApp().run()