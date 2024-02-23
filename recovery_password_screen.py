from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<RecoverPasswordScreen>:
    name:"recovery_password_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"300dp"
                MDIconButton:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon_size:"30dp"
                    icon:"arrow-left-top"
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
            Widget:
        MDBoxLayout:
            orientation:"vertical"
            padding:5
            spacing:"10dp"
            Widget:
            BoxLayout:
                size_hint_y:None
                height:"50dp"
                Widget:
                MDTextField:
                    size_hint_x:None
                    width:"300dp"
                    hint_text:"Email"
                    helper_text: "address@gmail.com"
                    line_color_normal:"red"
                    hint_text_color_normal:"red"
                    validator:"email"
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"30dp"
                Widget:
                SendVerificationCodeButton:
                    size_hint:None, None
                    height:"30dp"
                    width:"300dp"
                    radius:[20, 20, 20, 20]
                    md_bg_color:[0, 0/float(255), 0/float(255), 1]
                    MDLabel:
                        text:f"[color=#FFFFFF][font=Roboto]Send Verification Code[/font] [font=RobotoMedium][/font] [font=Icons]{md_icons['barcode']}[/font][/color]"
                        markup:True
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        color:[1, 1, 1, 1]
                Widget:
            Widget:
       
""")
class RecoverPasswordScreen(MDScreen):
    pass
class SendVerificationCodeButton(MDBoxLayout):
    pass
