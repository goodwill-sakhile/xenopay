from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, WipeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from load import LoadingScreen
from touch import TouchBox
from response import ResponseScreen
import time
import _thread as thread
from kivy.clock import Clock
ui = Builder.load_string("""
<LoadScreen>:
    name:"load_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            Widget:
            MDBoxLayout:
                size_hint:None, None
                size:"100dp", "100dp"
                padding:25, 25, 25, 25
                radius:[20, 20, 20, 20]
                md_bg_color:[0, 0, 0, 1]
                Image:
                    id:gif
                    source:"load.gif"
                    center:self.parent.center
                    size:50, 50
                    allow_stretch:True
                    anim_delay:-1
                    anim_loop:10000000000000000000000000
                    #_coreimage:anim_reset(True)
                    anim_delay:0.01
            Widget:
        MDBoxLayout:
<UserRequestBox>:
    id:user_request_box
    size_hint_y:None
    height:"110dp"
    orientation:"vertical"
    padding:5
    md_bg_color:[60/float(255), 51/float(255), 129/float(255), 1]
    radius:[20, 20, 20, 20]
    MDBoxLayout:
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[40, 40, 40, 40]
            pos_hint:{"center_y":.5}
            md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
            MDLabel:
                id:first_letter
                text:"S"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        MDBoxLayout:
            orientation:"vertical"
            padding:"5dp", "0dp"
            MDLabel:
                id:email_address_label
                text:"sakhile@gmail.com"
                text_size:self.size
                halign:"left"
                valign:"middle"
                color:[180/float(255), 180/float(255), 180/float(255), 1]
            MDBoxLayout:
                MDIcon:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"loupe"
                    theme_text_color:"Custom"
                    text_color:[130/float(255), 130/float(255), 135/float(255), 1]
                    pos_hint:{"center_y":.5}
                MDLabel:
                    id:amount_label
                    text:"Request amount is R1200"
                    text_size:self.size
                    halign:"left"
                    valign:"middle"
                    color:[130/float(255), 130/float(255), 135/float(255), 1]  
    MDBoxLayout:
        spacing:5
        Widget:
        ApproveButtonBox:
            root:user_request_box
            size_hint_x:None
            width:"100dp"
            size_hint_y:None
            height:"40dp"
            radius:[30, 30, 30, 30]
            md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
            pos_hint:{"center_y":.5}
            MDLabel:
                text:"Approve"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[0, 0, 0, 1]
        DeclineButtonBox:
            root:user_request_box
            size_hint_x:None
            width:"100dp"
            size_hint_y:None
            height:"40dp"
            radius:[30, 30, 30, 30]
            md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
            pos_hint:{"center_y":.5}
            MDLabel:
                text:"Decline"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        Widget:
<MoneyRequestsScreen>:
    name:"money_requests_screen"
    id:requests_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"5dp", "5dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[20, 20, 0, 0]
            size_hint_y:None
            height:"80dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"arrow-left-thick"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackHome()
            MDLabel:
                text:"Requests (0)"
                font_size:"23dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[0, 0, 20, 20]
            orientation:"vertical"
            ScreenManager:
                id:requests_body_screen_manager
                MDScreen:
                    name:"money_requests_user_list_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        padding:10, 10, 10, 10
                        MDBoxLayout:
                            FloatLayout:
                                pos:self.parent.pos
                                size_hint:None, None
                                size:self.parent.size
                                MDBoxLayout:
                                    pos:self.parent.pos
                                    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                                    radius:[20, 20, 20, 20]
                                    orientation:"vertical"
                                    ScrollView:
                                        size_hint:None, None
                                        size:self.parent.size
                                        bar_with:0
                                        MoneyRequestsLayout:
                                            root:requests_screen
                                MDBoxLayout:
                                    ScreenManager:
                                        id:loading_space
                                        MDScreen:
                                            name:"empty_screen"
                                        LoadScreen:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"50dp"
                            padding:0, 10, 0, 0
                            MDBoxLayout:
                                radius:[30, 30, 30, 30]
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                MDLabel:
                                    text:"Delete all requests"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
""")
class LoadScreen(MDScreen):
    pass
class ApproveButtonBox(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = 0
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/approve_request/", params = self.params).text)
            if response[0]  == 1:
                self.id = response[1]
                self.response = 1
        except:
            self.response = -2
    def determineNextScreen(self, seconds):
        if self.response == 1:
            button = MDFillRoundFlatButton(text = "Ok")
            self.unscheduleLoadingState()
            button.bind(on_release = self.close)
            self.callDialog("Feedback", "Amount was deducted from your account", button)
            self.root.parent.remove_widget(self.root)
        elif self.response == -2:
            button = MDFillRoundFlatButton(text = "Ok")
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog("Feedback", "Network connection failure", button)
            button.bind(on_release = self.close)
        else:
            Clock.schedule_once(self.determineNextScreen, 0)
    def addLoadingScreen(self):
        self.root.parent.root.ids.loading_space.transition = SlideTransition(direction = "left")
        self.root.parent.root.ids.loading_space.current = "load_screen"
    def unscheduleLoadingState(self):
        self.root.parent.root.ids.loading_space.transition = SlideTransition(direction = "left")
        self.root.parent.root.ids.loading_space.current = "empty_screen"
        Clock.unschedule(self.makeRequest)
        Clock.unschedule(self.determineNextScreen)
    def callDialog(self, title, text, button):
        self.dialog = MDDialog(title = title, text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
    def respondToTouch(self):
        self.addLoadingScreen()
        Clock.schedule_once(self.makeRequest, 0)
        Clock.schedule_once(self.determineNextScreen, 3)
class DeclineButtonBox(TouchBox):
    def respondToTouch(self):
        print("Decline")
        print("Parent is : ", self.root.parent)
        self.root.parent.remove_widget(self.root)
class UserRequestBox(MDBoxLayout):
    pass
class MoneyRequestsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.requests_layout = [["mailaddress@gmail.com", "6000"], ["emailaddress@yahoo.com", "200"]]
        self.size_hint_y = None
        self.spacing = 10
        self.padding = ("10dp", "10dp")
        self.bind(minimum_height = self.setter("height"))
        for r_info in self.requests_layout:
            user_request_bar = UserRequestBox()
            user_request_bar.ids.first_letter.text = r_info[0][0].upper()
            user_request_bar.ids.email_address_label.text = r_info[0]
            user_request_bar.ids.amount_label.text = "Request amount is R" + r_info[1]
            self.add_widget(user_request_bar)
class MoneyRequestsScreen(MDScreen):
    def goBackHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
class TestApp(MDApp):
    def build(self):
        root = MoneyRequestsScreen()
        return root
if __name__ == "__main__":
    TestApp().run() 