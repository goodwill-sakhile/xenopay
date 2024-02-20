from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder 
root = Builder.load_string("""
<DigitTextBox>:
	size_hint:None, None
	size:"50dp", "50dp"
	md_bg_color:1, 1, 1, 1
	padding:5
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
<DigitSpaceBox>:
	size_hint:None, None
	height:"400dp"
	width:"300dp"
	MDGridLayout:
		spacing:10
		cols:3
		rows:4
		size_hint:None, None
		size:"300dp", "300dp"
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"1"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"2"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"3"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"4"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"5"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"6"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"7"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"8"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"9"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			Widget:
			MDIconButton:
				size_hint:None, None
				size:"50dp", "50dp"
				icon:"refresh"
				icon_size:"30dp"
				pos_hint:{"center_x":.5, "center_y":.5}
			Widget:
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			MDLabel:
				text:"0"
				text_size:self.size
				halign:"center"
				valign:"middle"
				font_size:"20dp"
				color:0, 0, 0, 1
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			radius:10, 10, 10, 10
			Widget:
			MDIconButton:
				size_hint:None, None
				size:"50dp", "50dp"
				icon:"close"
				icon_size:"30dp"
				pos_hint:{"center_x":.5, "center_y":.5}
			Widget:
<CodeVerificationScreen>:
	name:"code_verification_screen"
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
					icon_size:"30dp"
					icon:"arrow-left-top"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
				Widget:
			Widget:
		MDBoxLayout:
			orientation:"vertical"
			spacing:15
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				spacing:15
				Widget:
				DigitTextBox:
				DigitTextBox:
				DigitTextBox:
				DigitTextBox:
				Widget:
			MDBoxLayout:
				size_hint_y:None
				width:"10dp"
			MDBoxLayout:
				size_hint_y:None
				height:"30dp"
				Widget:
				MDBoxLayout:
					radius:20, 20, 20, 20
					size_hint:None, None
					size:"300dp", "30dp"
					md_bg_color:0, 154/float(255), 255/float(255), 1
					MDLabel:
						text:"Verification code"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"30dp"
				Widget:
				MDBoxLayout:
					radius:20, 20, 20, 20
					size_hint:None, None
					size:"300dp", "30dp"
					md_bg_color:0, 0, 0, 1
					MDLabel:
						text:"Resend code"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"300dp"
				Widget:
				DigitSpaceBox:
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"30dp"
""")
class DigitTextBox(MDBoxLayout):
	pass
class DigitSpaceBox(MDBoxLayout):
	pass
class CodeVerificationScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = CodeVerificationScreen()
		return root
if __name__ == "__main__":
	TestApp().run()