from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang  import Builder
root = Builder.load_string("""
<LoadScreen>:
	name:"load_screen"
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
		Image:
			size_hint:None, None
			size:"60dp", "60dp"
			source:"03-42-11-849_512.gif"
			pos_hint:{"center_x":.5, "center_y":.5}
			allow_stretch:True
            anim_delay:-1
            anim_loop:10000000000000000000000000
            #_coreimage:anim_reset(True)
            anim_delay:0.01
		MDBoxLayout:
""")
class LoadScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = LoadScreen()
		return root
if __name__ == "__main__":
	TestApp().run()