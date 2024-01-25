from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
root = Builder.load_string("""
<SignUpScreen>:
    name:"sign_up_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout
            size_hint_y:None
            height:"50dp"
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"300dp"
                MDIconButton:
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[220/float(255), 220/float(255), 220/float(255), 1]
                    icon:"arrow-left-top"
                    pos_center:{"center_x":.5, "center_y":.5}
                    on_press:root.goBackToLoginScreen()
                Widget:
            Widget:
        Widget:
        MDBoxLayout:
            Widget:
            MDTextField:
                size_hint_x:None
                width:"300dp"
                hint_text:"First Name"
                icon_right_color_normal:"white"
                line_color_normal:"red"
                hint_text_color_normal:"red"
            Widget:
        MDBoxLayout:
            Widget:
            MDTextField:
                size_hint_x:None
                width:"300dp"
                hint_text:"Surname"
                icon_right_color_normal:"white"
                line_color_normal:"red"
                hint_text_color_normal:"red"
            Widget:
        MDBoxLayout:
            Widget:
            MDTextField:
                size_hint_x:None
                width:"300dp"
                hint_text:"Email Address"
                icon_right_color_normal:"white"
                line_color_normal:"red"
                hint_text_color_normal:"red"
            Widget:
        MDBoxLayout:
            Widget:
            MDTextField:
                size_hint_x:None
                width:"300dp"
                hint_text:"Password"
                icon_right_color_normal:"white"
                line_color_normal:"red"
                hint_text_color_normal:"red"
            Widget:
        MDBoxLayout:
            Widget:
            MDTextField:
                size_hint_x:None
                width:"300dp"
                hint_text:"Verify Password"
                icon_right_color_normal:"white"
                line_color_normal:"red"
                hint_text_color_normal:"red"
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp"
            Widget
            SignUpBox:
                size_hint:None, None
                height:"30dp"
                width:"300dp"
                radius:[20, 20, 20, 20]
                md_bg_color:[0, 0/float(255), 0/float(255), 1]
                MDLabel:
                    text:f"[color=#FFFFFF][font=Roboto]Sign Up[/font] [font=RobotoMedium][/font] [font=Icons]{md_icons['account-convert']}[/font][/color]"
                    markup:True
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
            Widget:
        Widget:
""")
class SignUpScreen(MDScreen):
    def goBackToLoginScreen(self):
        self.parent.trasition = SlideTransition(direction = "right")
        self.parent.current = "login_screen"

