from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<LoginScreen>:
    name:"login_screen"
    id:login_screen
    MDBoxLayout:
    FloatLayout:
            #pos_hint:None, None
            pos:self.parent.pos
            size:self.parent.size
            radius:[30, 30, 0, 0]
            MDBoxLayout
            	#pos:self.parent.pos
            	#md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
          	  orientation:"vertical"
         	   Widget:
            	MDBoxLayout:
               	 size_hint_y:None
                	height:"60dp"
                	Widget:
                	MDTextField:
                 	   root:login_screen
                   	 id:email_login_object
                    	size_hint_x:None
                    	width:"300dp"
                    	hint_text:"Email"
                    	helper_text: "address@gmail.com"
                    	validator:"email"
                	Widget:
            	Widget:
            MDBoxLayout:
            	pos:self.parent.pos
				ScreenManager:
					MDScreen:
						name:"empty" 
					MDScreen: 
				    	name:"pop_up_screen"
""")	
class LoginScreen(MDScreen):
    def goToPasswordReset(self):
    	print("Hello Password recovery screen")
    	self.parent.transition = SlideTransition(direction = "left")
    	self.parent.current = "recovery_password_screen"
class SignUpBox(TouchBox):
    def respondToTouch(self):
        print("Respond to touch")
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "sign_up_screen"
class LoginButtonBox(TouchBox):
    def respondToTouch(self):
        email = self.root.ids.email_login_object.text
        password = self.root.ids.password_login_object.text
        print(email, password)