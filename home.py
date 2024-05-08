from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import SlideTransition
from load_screen import LoadScreen
import time
import _thread as thread
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<ItemSpaceBox>:
	radius:20, 20, 20, 20
	orientation:"vertical"
	size_hint_y:None
	height:"500dp"
	md_bg_color:57/float(255), 87/float(255), 87/float(255), 1
	MDBoxLayout:
		FitImage:
			id:item_image
			size_hint:None, None
			size:self.parent.size
			source:""
	MDBoxLayout:
		size_hint_y:None
		height:"70dp"
		padding:10
		spacing:10
		MDIconButton:
			md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
			icon:"cart-arrow-down"
			size_hint:None, None
			size:"30dp", "30dp"
			pos_hint:{"center_x":.5, "center_y":.5}
			icon_size:"30dp"
			theme_text_color:"Custom"
			text_color:0, 250/float(255), 154/float(255), 1
		MDIconButton:
			md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
			icon:"cart-arrow-up"
			size_hint:None, None
			size:"30dp", "30dp"
			pos_hint:{"center_x":.5, "center_y":.5}
			icon_size:"30dp"
			theme_text_color:"Custom"
			text_color:220/float(255), 20/float(255), 60/float(255), 1
		
<RoundShopIcon>:
	size_hint:None, None
	size:"50dp", "50dp" 
	image:""
	md_bg_color:1, 1, 1, 1
	radius:50, 50, 50, 50
	Widget:
	MDBoxLayout:
		md_bg_color:0, 0, 0, 1
		size_hint:None, None
		size:"45dp", "45dp"
		radius:45, 45, 45, 45
		pos_hint:{"center_x":.5, "center_y":.5}
		FitImage:
			size_hint:None, None
			size:"45dp", "45dp"
			radius:45, 45, 45, 45
			source:root.image
	Widget:
<HomeScreen>:
	name:"home_screen"
	id:home_screen
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		MDBoxLayout:
			orientation:"vertical"
			padding:5
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				md_bg_color:0, 0, 0, 1
				MDBoxLayout:
					size_hint_x:None
					width:"50dp"
					orientation:"vertical"
					Widget:
					MDIconButton:
						size_hint:None, None
						size:"40dp", "40dp" 
						icon:"logout"
						icon_size:"30dp"
						theme_text_color:"Custom"
						pos_hint:{"center_x":.5, "center_y":.5}
						text_color:1, 1, 1, 1
				MDBoxLayout:
					MDLabel:
						text:"Xenoshops"
						text_size:self.size
						halign:"center"
						valign:"middle"
						font_size:"18dp"
						color:1, 1, 1, 1
				MDBoxLayout:
					size_hint_x:None
					width:"50dp"
					orientation:"vertical"
					Widget:
					MDIconButton:
						size_hint:None, None
						size:"40dp", "40dp"
						icon:"cart-arrow-down"
						icon_size:"30dp"
						theme_text_color:"Custom"
						text_color:1, 1, 1, 1
						pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				Widget: 
				MDBoxLayout:
					size_hint_x:None
					width:"400dp" 
					orientation:"vertical"
					MDBoxLayout:
						size_hint_y:None
						height:"60dp"
						padding:10
						RoundShopIcon:
						Widget:
						MDBoxLayout:
							size_hint_x:None
							width:"60dp"
							MDIconButton: 
								icon:"filter-cog-outline"
								size_hint:None, None
								size:"40dp", "40dp"
								icon_size:"30dp"
					MDBoxLayout: 
						orientation:"vertical"
						ScreenManager:
							id:body_screen_manager
							MDScreen:
								name:"items_list_screen"
								MDBoxLayout:
									ScrollView:
										size_hint:None, None
										size:self.parent.size
										bar_width:0
										ItemsListLayout:
							LoadScreen:
							MDScreen:
								name:"empty_screen"
					MDBoxLayout:
						size_hint_y:None
						height:"80dp"
						padding:10
						MDBoxLayout:
							size_hint_y:None
							height:"60dp"
							radius:60, 60, 60, 60
							md_bg_color:0, 0, 0, 1
							padding:5
							Widget:
							RoundShopIcon:
								root:home_screen
								image:"picknpay.png"
								pos_hint:{"center_x":.5, "center_y":.5}
							Widget:
							RoundShopIcon:
								root:home_screen
								image:"shoprite.png"
								pos_hint:{"center_x":.5, "center_y":.5}
							Widget:
							RoundShopIcon:
								root:home_screen
								image:"checkers.png"
								pos_hint:{"center_x":.5, "center_y":.5}
							Widget:
							RoundShopIcon:
								root:home_screen
								image:"woolworths.jpeg"
								pos_hint:{"center_x":.5, "center_y":.5}
							Widget:
							RoundShopIcon:
								root:home_screen
								pos_hint:{"center_x":.5, "center_y":.5}
							Widget:
							MDIconButton:
								size_hint:None, None
								size:"50dp", "50dp"
								icon:"skew-more"
								theme_text_color:"Custom"
								text_color:1, 1, 1, 1
								icon_size:"30dp"
								pos_hint:{"center_x":.5, "center_y":.5}
				Widget:
""")
class ItemSpaceBox(MDBoxLayout):
	pass
class ItemsListLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.size_hint_y = None
		self.spacing = 10
		self.bind(minimum_height = self.setter("height"))
		self.items = ["item_1", "item_2", "item_3",  "item_4"]
		self.stackItems()
	def stackItems(self):
		for image in self.items:
			item = ItemSpaceBox()
			item.ids.item_image.source = image
			self.add_widget(item)
class RoundShopIcon(TouchBox):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.next_shop_screen = ""
	def respondToTouch(self):
		if self.root.ids.body_screen_manager.current != "load_screen":
			self.switchToLoadingScreen()
	def switchToLoadingScreen(self):
		self.root.ids.body_screen_manager.transition  = SlideTransition(direction = "left")
		self.root.ids.body_screen_manager.current = "load_screen"
		thread.start_new_thread(self.prepareToMoveToNextShop, ( ))
	def prepareToMoveToNextShop(self):
		time.sleep(2)
		self.root.ids.body_screen_manager.transition  = SlideTransition(direction = "left")
		self.root.ids.body_screen_manager.current = "empty_screen"
class HomeScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = HomeScreen()
		return root
if __name__ == "__main__":
	TestApp().run()