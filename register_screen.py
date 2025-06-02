import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<SubScreenOneForwardButton>
    size_hint_y:None
    height:"40dp"
    md_bg_color:0, 0, 0, 1
    radius:20, 20, 20, 20
    MDLabel:
        text:"Continue"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
<RegisterScreen>:
    name:"register_screen"
    id:register_user_details
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            MDIconButton:
                icon:"arrow-left"
                pos_hint:{"center_x":.5, "center_y":.5}
                size_hint:None, None
                size:"40dp", "40dp"
        MDBoxLayout:
            Widget:
            MDBoxLayout:
                sizer_hint_x:None
                width:"300dp"
                orientation:"vertical"
                Widget:
                MDTextField:
                    id:names_text_box
                    hint_text:"Full Name (s)"
                    icon_left:"account"
                    theme_line_color:"Custom"
                    line_color_normal:0, 0, 0, 1
                    mode:"line"
                MDTextField:
                    id:surname_text_box
                    hint_text:"Surname"
                    icon_left:"account"
                    thme_line_color:"Custom"
                    line_color_normal:0, 0, 0, 1
                    mode:"line"
                MDTextField:
                    id:email_text_box
                    hint_text:"Email"
                    icon_left:"email"
                    theme_line_color:"Custom"
                    line_color_normal:0, 0, 0, 1
                    mode:"line"
                MDTextField:
                    id:password_text_box
                    hint_text:"Password"
                    icon_left:"onepassword"
                    theme_line_color:"Custom"
                    line_color_normal:0, 0, 0, 1
                    mode:"line"
                MDTextField:
                    id:password_two_text_box
                    hint_text:"Confirm Password"
                    icon_left:"onepassword"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    theme_line_color:"Custom"
                    line_color_normal:0, 0, 0, 1
                    mode:"line"
                MDBoxLayout:
                    size_hint_y:None
                    height:"50dp"
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:10
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"300dp"
                SubScreenOneForwardButton
                    root:register_user_details
            Widget:
""")
class SubScreenOneForwardButton(TouchBox):
    def __init__(self, **kwargs):
        self.user_params = {}
    def respondToTouch(self):
        pass
    def getAllUserDetails(self):
        print(self.root.ids)
        names = self.root.ids.names_text_box
        surname = self.root.ids.surname_text_box
        email = self.root.ids.email_text_box
    def validateEmail(self, email):
        if "@" in email:
            divider = email.index("@")
            email_domain = email[divider + 1:]
            if "." in email_domain:
                return True
        else:
            False
    def checkIfTextFieldEmpty(self, user_data):
        if not user_data:
            True
        else:
            False
    def comparePasswordMatch(self)
        password_one = self.root.ids.password_text_box
        password_two = self.root.ids.password_two_text_box
        if password_one == passowrd_two:
            True
        else:
            False
class RegisterScreen(MDScreen):
    pass
class RegisterTestApp(MDApp):
    def build(self):
        root = RegisterScreen()
        return root
if __name__ == "__main__":
    RegisterTestApp().run()
