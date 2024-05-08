from kivymd.app import MDapp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import RiseInTransition
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<ItemCounterRoundBox>:
	radius:[20, 20, 20, 20]
	size_hint:None, None
	size:"30dp", "30dp"
	md_bg_color:0, 0, 0, 1
	id:items_counter_round_box
	MDLabel:
		root:items_counter_round_box
		id:counter
		text:"0"
		text_size:self.size
		halign:"center"
		valign:"middle"
		md_bg_color:1, 1, 1, 1
<ItemOnCartBox>:
	size_hint:None, None
	size:"145dp", "145dp"
	FloatLayout:
		size_hint:None, None
		size:self.parent.size
		pos_hint:None, None
		pos:self.parent.pos
		MDBoxLayout:
			pos_hint:None, None
			pos:self.parent.pos
			FitImage:
				id:item_image
				size_hint:None, None
				size:self.parent.size
				source:""
		MDBoxLayout:
			pos_hint:None, None
			pos:self.parent.pos
			orientation:"vertical"
			MDBoxLayout:
				size_hint_y:None
				height:"30dp"
				padding:"5dp", "0dp"
				spacing:2
				Widget:
				ItemCounterRoundBox:
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"close"
					md_bg_color:0, 0, 0, 1
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_y:None
				height:"30dp"
				spacing:3
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					Icon:"minus"
					md_bg_color:0, 0, 0, 1
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
				MDIconButton: 
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"plus"
					md_bg_color:0, 0, 0, 1
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
<CartInfoBox>:
	id:cart_info_box
	md_bg_color:47/float(255), 79/float(255),  79/float(255), 0.5
	size_hint_y:None
	heigt:"60dp"
	padding:5
	spacing:5
	orientation:"vertical"
	MDBoxLayout:
		MDLabel:
			id:total_amount
			text:"Total Amount: R0, 00"
			text_size:self.size
			halign:"left"
			valign:"middle"
			color:1, 1, 1, 1
	MDBoxLayout:
		MDLabel:
			id:total items
			text:"Total Items [10]"
			text_size:self.size
			halign:"left"
			valign:"middle"
			color:1, 1, 1, 1
<PayButton>:
	size_hint_y:None
	height:"30dp"
	md_bg_color:0, 154/float(255), 255/float(255), 1
	radius:30, 30, 30, 30
	MDLabel:
		text:"Pay"
		text_size:self.size
		halign:"center"
		valign:"middle"
		color:1, 1, 1, 1
<CartScreen>:
	name:"cart_screen"
	id:cart_screen
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		padding:5
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			md_bg_color:0, 0, 0, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				Widget:
				MDIconButton:
					icon:"arrow-left-bold"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					size_hint:None, None
					size:"50dp", "50dp"
					icon_size:"30dp"
			MDLabel:
				text:"Cart"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"25dp"
				color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			size_hint_x:None
			width:"300dp"
			orientation:"vertical"
			CartInfoBox:
			FloatLayout:
				size_hint:None, None
				pos_hint:None, None
				size:self.parent.size 
				pos:self.parent.pos
				MDBoxLayout:
					pos_hint:None, None
					pos:self.parent.pos
					ScrollView:
						size_hint:None, None
						size:self.parent.size
						CartItemsLayout:
				MDBoxLayout:
					pos_hint:None, None
					pos:self.parent.pos
					ScreenManager:
						id:pop_up_screen_manager
						MDScreen:
							name:"empty_screen"
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				padding:"0dp", "10dp"
				PayButton:
					root:cart_screen
""")
class ItemCounterRoundBox(MDBoxLayout):
	pass
class ItemOnCartBox(TouchBoxLayout):
	def respondToTouch(self):
		pass
class CartInfoBox(MDBoxLayout):
	pass
class PayButton(TouchBox):
	def respondToTouch(self):
		self.root.ids.pop_up_screen_manager.transition = RiseInTransition()
		self.root.ids.pop_up_screen_manager.current = "Pay_pin_popup_screen"
class CartScreen(MDScreen):
	def goBackToHome(self):
		self.parent.transition = SlideTransition(direction = "right")
		self.parent.current = "home_screen"