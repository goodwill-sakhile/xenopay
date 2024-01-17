from kivymd.app import MDApp 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
root = Builder.load_string("""
<TransactionBar>:
	size_hint_y:None
	height:"70dp"
	orientation:"vertical"
	MDBoxLayout:
		size_hint_y:None
		height:"69dp"
		MDBoxLayout:
			orientation:"vertical"
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				MDLabel:
					text:"Sender"
					bold:True
					font_size:"20dp"
					text_size:self.size
					halign:"left"
					valign:"middle"
			MDBoxLayout:
				size_hint_y:None
				height:"19dp"
				MDLabel:
					text:"10/10/2024"
					text_size:self.size
					halign:"left"
					valign:"middle"
		MDBoxLayout:
			size_hint_x:None
			width:"100dp"
			MDLabel:
				text:"+R200"
				bold:True
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"18dp"
				color:0, 255/float(255), 100/float(255), 1
	MDBoxLayout:
		md_bg_color:0, 0, 0, 1
		size_hint_y:None
		height:"1dp"
<CashInScreen>:
	name:"cash_in_screen"
	MDBoxLayout:
		orientation:"vertical"
		ScrollView:
			size_hint:None, None
			size:self.parent.size
			CashInGridLayout:
				cols:1
<CashOutScreen>:
	name:"cash_out_screen"
<AccountTransactionHistoryScreen>:
	name:"account_transaction_history_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon_size:"30dp"
					icon:"arrow-left-top"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
					on_press:self.goBackToHome()
			MDBoxLayout:
				MDLabel:
					text:"Transaction History"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:1, 1, 1, 1
					font_size:"25dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
				orientation:"vertical"
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					MDLabel:
						text:"Account Balance"
						text_size:self.size
						halign:"left"
						valign:"middle"
						color:1, 1, 1, 1
						font_size:"23dp"
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					padding:"10dp", "0dp"
					MDLabel:
						text:"R629.67"
						text_size:self.size
						halign:"left"
						valign:"middle"
						color:1, 1, 1, 1
						font_size:"19dp"
				MDBoxLayout:
					size_hint_y:None
					height:"1dp"
					md_bg_color:0, 154/float(255), 255/float(255), 1
				MDBoxLayout:
					size_hint_y:None
					height:"50dp"
					padding:"0dp", "10dp"
					spacing:15
					MDBoxLayout:
						size_hint_y:None
						height:"30dp"
						radius:20, 20, 20, 20
						md_bg_color:220/float(255),  220/float(255), 220/float(255), 1
						MDLabel:
							text:"Cash-In"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:0, 0, 0, 1
					MDBoxLayout:
						size_hint_y:None
						height:"30dp"
						radius:20, 20, 20, 20
						md_bg_color:0, 0/float(255), 0/float(255), 1
						MDLabel:
							text:"Cash-Out"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					ScreenManager:
						CashInScreen:
						CashOutScreen:
			Widget:
""")
class TransactionBar(MDBoxLayout):
	pass
class CashInGridLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.size_hint_y = None
		self.bind(minimum_height = self.setter("height"))
		self.addCashInBars()
	def addCashInBars(self):
		for i in range(15):
			bar = TransactionBar()
			self.add_widget(bar)
class CashInScreen(MDScreen):
	pass
class CashOutScreen(MDScreen):
	pass
class AccountTransactionHistoryScreen(MDScreen):
	def goBackToHome(self):
		self.parent.transition = SlideTransition(direction = "right")
		self.parent.current = "home_screen"
class TestApp(MDApp):
	def build(self):
		root = AccountTransactionHistoryScreen()
		return root
if __name__ == "__main__":
	TestApp().run()