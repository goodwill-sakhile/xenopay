from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from who_to_pay import WhoToPayScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.button import MDIconButton
from touch import TouchBox
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
<PayScreen>:
    name:"pay_screen"
    id:pay_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"5dp", "5dp"
        spacing:5
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                theme_text_color: "Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                icon:"arrow-left-thick"
                on_release:root.goBackToHomeScreen()
            MDLabel:
                text:"Pay"
                font_size:"23dp"
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[20, 20, 20, 20]
            orientation:"vertical"
            MDBoxLayout:
                pos:self.parent.pos
                size_hint_y:None
                height:"50dp"
                MDLabel:
                    text:"R0"
                    font_size:"24dp"
                    bold:True
                    color:[1, 1, 1, 1]
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    id:amount
            MDBoxLayout:
                FloatLayout:
                    size_hint:None, None
                    size:self.parent.size
                    pos:self.parent.pos
                    MDBoxLayout:
                        pos:self.parent.pos
                        root:pay_screen
                        MDBoxLayout:
                        DigitLayout:
                            size_hint_x:None
                            width:"300dp"
                            md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                            radius:[20, 20, 20, 20]
                        MDBoxLayout:
                    MDBoxLayout:
                        pos:self.parent.pos
                        ScreenManager:
                            id:loading_space
                            MDScreen:
                                name:"empty_screen"
                            LoadScreen:
            MDBoxLayout:
                root:pay_screen
                size_hint_y:None
                height:"60dp"
                padding:10, 0, 10, 15
                ContinueButtonBox:
<DigitButtonBox>:
    size_hint_x:None
    width:"100dp"
    padding:"20dp", "0dp"
<ButtonBox>:
    text:""
    size_hint_y:None
    height:"40dp"
    radius:[30, 30, 30, 30]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    MDLabel:
        text:root.text
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:[1, 1, 1, 1]
<ContinueButtonBox>:
    text:"Continue"
<RequestButtonBox>:
    text:"Request"
""")
class ButtonBox(TouchBox):
    pass
class ContinueButtonBox(ButtonBox):
    def respondToTouch(self):
        self.goToLoadingScreen()
        Clock.schedule_once(self.goToWhoToPayScreen, 1)
    def goToLoadingScreen(self):
        self.parent.root.ids.loading_space.transition = SlideTransition(direction = "left")
        self.parent.root.ids.loading_space.current = "load_screen"
    def unscheduleLoadingState(self):
        self.parent.root.ids.loading_space.transition = SlideTransition(direction = "left")
        self.parent.root.ids.loading_space.current = "empty_screen"
    def goToWhoToPayScreen(self, seconds):
        try:
            if float(self.parent.root.amount) > 0:
                print("Amount :", self.parent.root.amount)
                print("Does it exist :")
                if not self.parent.root.parent.has_screen("who_to_pay_screen"):
                    print("Add Who_To_Pay_Screen ")
                    who_to_pay_screen = WhoToPayScreen()
                    who_to_pay_screen.amount = int(self.parent.root.amount)
                    who_to_pay_screen.wallet_balance = self.parent.root.wallet_balance
                    self.parent.root.parent.add_widget(who_to_pay_screen)
                self.parent.root.parent.transition = SlideTransition(direction = "left")
                self.parent.root.parent.current = "who_to_pay_screen"
                self.parent.root.parent.ids.who_to_pay_object.ids.screen_title.text = "Who to Pay?"
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.transition = NoTransition()
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.current = "pay_someone_screen"
        except:
            pass
        self.unscheduleLoadingState()
class LoadScreen(MDScreen):
    pass
class DigitButtonBox(MDBoxLayout):
    pass
class DigitLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.putDigit()
    def putDigit(self):
        for char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0", "*"]:
            print("Character : ", char)
            if char == "*":
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "close", user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.cancel)
            elif char == ".":
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "circle-small", user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.enterDot)
            else:
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "numeric-" + char, user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.enterDigit)
            digit_button = DigitButtonBox()
            digit_button.add_widget(button)
            self.add_widget(digit_button)
    def enterDigit(self, button):
        number = button.icon[-1]
        print("Number :", number )
        if self.parent.root.amount == "":
           if number == "0":
                return
        self.parent.root.amount = self.parent.root.amount + number
        print("Amount : ", self.parent.root.amount)
        self.parent.root.ids.amount.text = "R" + self.parent.root.amount
        print("Label text : ", self.parent.root.ids.amount.text)
    def enterDot(self, button):
        if "." not in self.parent.root.amount:
            if self.parent.root.amount == "":
                self.parent.root.amount = "0."
            else:
                self.parent.root.amount = self.parent.root.amount + "."
        self.parent.root.ids.amount.text = "R" + self.parent.root.amount
    def cancel(self, button):
        if self.parent.root.amount == "0" or self.parent.root.amount == "":
            self.parent.root.amount = ""
        elif len(self.parent.root.amount) == 1:
            self.parent.root.amount = ""
            self.parent.root.ids.amount.text = "R0"
        else:
            print("amount length : ", len(self.parent.root.amount))
            if (self.parent.root.amount[0]  == "0") and (len(self.parent.root.amount) == 2):
                print("The length is 2 indeed")
                self.parent.root.amount = ""
                self.parent.root.ids.amount.text = "R0"
            else:
                self.parent.root.amount = self.parent.root.amount[:-1]
                self.parent.root.ids.amount.text = "R" + self.parent.root.amount
class PayScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.amount = ""
        self.wallet_balance = 0
    def goBackToHomeScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"