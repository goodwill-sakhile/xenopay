from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<LoginScreen>:
    name:"login_screen"
    id:login_screen
    MDBoxLayout:
        MDBoxLayout:
            radius:[30, 30, 0, 0]
            #md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            orientation:"vertical"
            Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"60dp"
                Widget:
                MDTextField:
                    id:email_login_object
                    size_hint_x:None
                    width:"300dp"
                    hint_text:"Email"
                    helper_text: "address@gmail.com"
                    validator:"email"
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"60dp"
                Widget:
                MDTextField:
                    id:password_login_object
                    size_hint_x:None
                    width:"300dp"
                    hint_text:"Password"
                    helper_text: "*******"
                    validator:"email"
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:10
                Widget:
                LoginButtonBox:
                    root:login_screen
                    id:login_button_box
                    radius:[20, 20, 20, 20]
                    size_hint:None, None
                    size:"300dp", "30dp"
                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                    MDLabel:
                        text:f"[color=#FFFFFF][font=Roboto]Login[/font] [font=RobotoMedium][/font] [font=Icons]{md_icons['login']}[/font][/color]"
                        markup:True
                        text_size:self.size
                        halign:"center"
                        valign:"middle" 
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:5
                Widget:
                MDIconButton:
                    icon:"refresh"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    size_hint:None, None
                    size:"50dp", "50dp"
                Widget:
            Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:10
                Widget:
                SignUpBox:
                    root:login_screen
                    size_hint:None, None
                    height:"30dp"
                    width:"300dp"
                    radius:[20, 20, 20, 20]
                    md_bg_color:[0, 0/float(255), 0/float(255), 1]
                    MDLabel:
                        text:f"[color=#FFFFFF][font=Roboto]Register[/font] [font=RobotoMedium][/font] [font=Icons]{md_icons['account-convert']}[/font][/color]"
                        markup:True
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        color:[1, 1, 1, 1]
                        
                Widget:
""")	
class LoginScreen(MDScreen):
    pass
class SignUpBox(TouchBox):
    def respondToTouch(self):
        print("Respond to touch")
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "sign_up_screen"
class LoginButtonBox(TouchBox):
	def respondToTouch(self):
		email = self.root.ids.email_login_object
		password = self.root.ids
		print(email, password)