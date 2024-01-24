from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<HomeScreen>:
	name:"home_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
		MDBoxLayout:
			orientation:"vertical"
			Widget:
			MDBoxLayout:
				Widget:
				MDGridLayout:
					size_hint:None, None
					size:"300dp", "300dp"
					cols:2
					rows:2
					spacing:10
					padding:5
					MDBoxLayout:
						radius:10, 10, 10, 10
						md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
						orientation:"vertical"
						Widget:
						MDIconButton:
							icon:"wallet-plus"
							size_hint:None, None
							size:"50dp", "50dp"
							icon_size:"50dp"
							pos_hint:{"center_x":.5, "center_y":.5}
							theme_text_color:"Custom"
							text_color:1, 1, 1, 1
						Widget:
					MDBoxLayout:
						radius:10, 10, 10, 10
						md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
						Widget:
						MDIconButton:
							icon:"cash-fast"
							size_hint:None, None
							size:"50dp", "50dp"
							icon_size:"50dp"
							pos_hint:{"center_x":.5, "center_y":.5}
							theme_text_color:"Custom"
							text_color:1, 1, 1, 1
						Widget:
					MDBoxLayout:
						radius:10, 10, 10, 10
						md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
						Widget:
						MDIconButton:
							icon:"bank-transfer"
							size_hint:None, None
							size:"50dp", "50dp"
							icon_size:"50dp"
							pos_hint:{"center_x":.5, "center_y":.5}
							theme_text_color:"Custom"
							text_color:1, 1, 1, 1
						Widget:
					MDBoxLayout:
						radius:10, 10, 10, 10
						md_bg_color:57/float(255), 89/float(255), 89/float(255), 1
						Widget:
						MDIconButton:
							icon:"cog-transfer"
							size_hint:None, None
							size:"50dp", "50dp"
							icon_size:"50dp"
							pos_hint:{"center_x":.5, "center_y":.5}
							theme_text_color:"Custom"
							text_color:1, 1, 1, 1
						Widget:
				Widget:
			Widget:
""")
class HomeScreen(MDScreen):
	pass