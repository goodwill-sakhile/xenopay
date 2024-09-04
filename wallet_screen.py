from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen MDScreen
from kivy.uix.screenmanger import *
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Buildet
from touch import TouchBox
ui = Builder.load_string("""
<WalletAmountBox>:
	size_hint_y:None
	height:"60dp"
	radius:20, 20, 20, 20
	md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
	MDLabel:
		text:"Amount: R0.00"
		font_size:"18dp"
		text_size:self.size
		halign:"center"
		valign:"middle"
		color:1, 1, 1, 1
<CashInBarBox>:
	size_hint_y:None
	height:"50dp"
	padding:5
	spacing:5
	MDBoxLayout:
		size_hint:None, None
		size:"40dp", "40dp"
		radius:40, 40, 40, 40
		md_bg_color:0, 0, 0, 1
		MDLabel:
			text:"C"
			bold:True
			text_size:self.size
			halign:"center"
			valign:"middle"
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			MDLabel:
				text:"Name Surname (+200) Cash-in"
				text_size:self.size 
				halign:"left"
				valign:"middle"
				color:1, 1, 1, 1
		MDBoxLayout:
			MDLabel:
				text:"01/01/2024" 
				text_size:self.size
				halign:"left"
				valign:"middle"
				color: 195/float(255), 195/float(255), 195/float(255), 1
<WalletScreen>:
	nam::"wallet_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"80dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				Widget:
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"arrow-left-thick"
					icon_size:"30dp"
					pos_hint:{"center_x":.5, "center_y":.5}
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				MDLabel:
					text:"Wallet & Transaction History"
					text_size:self.size
					halign:"center"
					valign:"middle"
					font_size:"18dp"
					color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				spacing:5
				WalletAmountBox:
				MDBoxLayout:
					size_hint_y:None
					height:"50dp"
					padding:"5dp", "5dp"
					spacing:5
					CashInButtonBox:
						radius:30, 30, 30, 30
						size_hint_y:None
						height:"30dp"
						md_bg_color:0, 0, 0, 1
						MDLabel:
							text:"Cash-in"
							text_size:self.size
							halign:"center"
							valigb:"middle"
							color:1, 1, 1, 1
					CashOutButtonBox:
						radius:30, 30, 30, 30
						size_hint_y:None
						height:"30dp"
						md_bg_color:0, 154/float(255), 220/float(255), 1
						MDLabel:
							text:"Cash-out"
							text_size:self.size
							halign:"center"
							valigb:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					orientation:"vertical"
					ScrollView:
						size_hint:None, None
						size:self.parent.size
						TransactionHistroryListLayout:
			Widget:
""")
class TransactionHistroryListLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.spacing = 5
		self.bind(minimum_height = self.setter("height"))