from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from touch import TouchBox
from kivy.lang import Builder
from kivy.clock import Clock
ui = Builder.load_string("""
<UserBarBox>:
    size_hint_y:None
    height:"60dp"
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    padding:5
    MDBoxLayout:
        id:circle
        size_hint:None, None
        size:"50dp", "50dp"
        md_bg_color:[0, 1, 0, 1]
        radius:[40, 40, 40, 40]
        MDLabel:
            id:name_first_letter
            text:"S"
            text_size:self.size
            halign:"center"
            valign:"middle"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:email_address
                text:"email@address"
                text_size:self.size
                halign:"left"
                valign:"middle"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:user_name
                text:"username"
                text_size:self.size
                halign:"left"
                color:[100/float(255), 100/float(255), 100/float(255), 1]
                valign:"middle"
    MDIconButton:
        id:icon_button
        size_hint:None, None
        size:"40dp", "40dp"
        pos_hint:{"center_x":.5, "center_y":.5}
        icon:"checkbox-multiple-blank-circle"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
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
<WhoToPayScreen>:
    name:"who_to_pay_screen"
    id:who_to_pay_screen
    MDBoxLayout:
        orientation:"vertical"
        padding:"10dp", "5dp"
        md_bg_color:[0, 0, 0, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"130dp"
            md_bg_color:[72/float(255), 62/float(255), 139/float(255), 1]
            radius:[20, 20, 0, 0]
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                MDIconButton:
                    size_hint:None, None
                    size:"50dp", "50dp"
                    icon:"arrow-left-thick"
                    user_font_size:"30dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    pos_hint:{"center_x":.5, "center_y":.5}
                    on_release:root.goBackToPayScreen()
                MDLabel:
                    id:screen_title
                    text:"Pay or Request"
                    font_size:"23dp"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDBoxLayout:
                    size_hint_x:None
                    width:"50dp"
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDIconButton:
                    icon:"account"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    user_font_size:"30dp"
                    pos_hint:{"center_y":.5}
                    theme_text_color:"Custom"
                    text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                MDBoxLayout:
                    MDLabel:
                        id:selected_users
                        text:"Selected users (0)"
                        text_size:self.size
                        valign:"middle"
                        color:[1, 1, 1, 1]
        MDBoxLayout:
            orientation:"vertical"
            radius:[0, 0, 20, 20]
            md_bg_color:[72/float(255), 62/float(255), 139/float(255), 1]
            MDBoxLayout:
                ScreenManager:
                    id:body_screen_manager
                    MDScreen:
                        name:"request_someone_screen"
                        MDBoxLayout:
                            FloatLayout:
                                size_hint:None, None
                                size:self.parent.size
                                pos:self.parent.pos
                                MDBoxLayout:
                                    pos:self.parent.pos
                                    orientation:"vertical"
                                    padding:10, 0, 10, 0
                                    MDBoxLayout:
                                        radius:[20, 20, 20, 20]
                                        padding:5, 15, 5, 15
                                        md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                                        MDBoxLayout:
                                            ScrollView:
                                                bar_width:0
                                                size_hint:None, None
                                                size:self.parent.size
                                                UsersListLayout:
                                                    root:who_to_pay_screen
                                    MDBoxLayout:
                                        root:who_to_pay_screen
                                        size_hint_y:None
                                        height:"50dp"
                                        padding:"0dp", "5dp", "0dp", "5dp"
                                        spacing:5
                                        RequestButtonBox:
                                            id:request_button_box
                                            radius:[30, 30, 30, 30]
                                            md_bg_color:[120/float(255), 120/float(255), 120/float(255), 1]
                                            MDLabel:
                                                text:"Request"
                                                text_size:self.size
                                                halign:"center"
                                                valign:"middle"
                                                color:[0, 0, 0, 1]
                                        SendButtonBox:
                                            id:send_button_box
                                            radius:[30, 30, 30, 30]
                                            md_bg_color:[120/float(255), 120/float(255), 120/float(255), 1]
                                            MDLabel:
                                                text:"Send"
                                                text_size:self.size
                                                halign:"center"
                                                valign:"middle"
                                                color:[0, 0, 0, 1]
                                MDBoxLayout:
                                    pos:self.parent.pos
                                    ScreenManager:
                                        id:loading_screen_manager
                                        MDScreen:
                                            name:"empty_screen"
                                        MDScreen:
                                            name:"loading_screen"
                                            LoadScreen:
            MDBoxLayout:
                size_hint_y:None
                height:"2dp"
""")
class UserBarBox(TouchBox):
    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
    def respondToTouch(self):
        if self.parent.root.touch_allowed:
            if self.ids.icon_button.icon == "checkbox-multiple-blank-circle":
                self.parent.root.user_counter += 1
                self.parent.root.ids.request_button_box.md_bg_color = [0, 154/float(255), 255/float(255), 1]
                self.parent.root.ids.request_button_box.children[0].color = [1, 1, 1, 1]
                self.parent.root.ids.send_button_box.md_bg_color = [0, 154/float(255), 255/float(255), 1]
                self.parent.root.ids.send_button_box.children[0].color = [1, 1, 1, 1]
                self.parent.root.ids.selected_users.text = "Selected users (" + str(self.parent.root.user_counter) + ")"
                self.ids.icon_button.icon = "checkbox-multiple-marked-circle"
                self.ids.icon_button.text_color = [0, 154/float(255), 255/float(255), 1]
            else:
                self.ids.icon_button.icon = "checkbox-multiple-blank-circle"
                self.parent.root.user_counter -= 1
                self.parent.root.ids.selected_users.text = "Selected users (" + str(self.parent.root.user_counter) + ")"
                if self.parent.root.user_counter == 0:
                    self.parent.root.ids.request_button_box.md_bg_color = [120/float(255), 120/float(255), 120/float(255), 1]
                    self.parent.root.ids.request_button_box.children[0].color = [0, 0, 0, 1]
                    self.parent.root.ids.send_button_box.md_bg_color = [120/float(255), 120/float(255), 120/float(255), 1]
                    self.parent.root.ids.send_button_box.children[0].color = [0, 0, 0, 1]
                self.ids.icon_button.text_color = [255/float(255), 255/float(255), 255/float(255), 1]
class LoadScreen(MDScreen):
    pass
class UsersListLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.padding = "5dp", "5dp"
        self.size_hint_y = None
        self.search_list = []
        self.bind(minimum_height = self.setter("height"))
        for i in range(10):
            bar = UserBarBox()
            self.add_widget(bar)
    def addUsersOnList(self):
        for info in self.search_list:
            bar = UserBarBox()
            bar.ids.name_first_letter.text = info[0]
            bar.ids.email_address.text = info[1]
            bar.ids.user_name.text = info[2]
            self.add_widget(bar)
class RequestButtonBox(TouchBox):
    def respondToTouch(self):
        total_amount = self.parent.root.amount * self.parent.root.user_counter
        if self.parent.root.user_counter:
            cancel_button = MDFillRoundFlatButton(text = "Cancel")
            request_button = MDFillRoundFlatButton(text = "Request")
            message = "Request R" + str(total_amount) + " from " + str(self.parent.root.user_counter) + " people?"
            self.parent.root.callDoubleButtonForAmountRequestDialog("Confirm amount request", message, cancel_button, request_button)
class SendButtonBox(TouchBox):
    def respondToTouch(self):
        total_amount = self.parent.root.amount * self.parent.root.user_counter
        if total_amount > 0:
            if total_amount <= self.parent.root.wallet_balance:
                cancel_button = MDFillRoundFlatButton(text = "Cancel")
                send_button = MDFillRoundFlatButton(text = "Send")
                message = "Totol amount is R" + str(total_amount)
                self.parent.root.callDoubleButtonForAmountSendDialog("Confirm transaction amount", message, cancel_button, send_button)
            else:
                message = "Insufficient funds, your wallet balance is R" + str(self.parent.root.wallet_balance)
                send_button = MDFillRoundFlatButton(text = "Ok")
                self.parent.root.callDialog("Transaction failure", message, send_button)
class WhoToPayScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_counter = 0
        self.amount = 20
        self.wallet_balance = 30
        self.touch_allowed = True
        self.response_message = ""
        self.error_message = ""
        self.params = {}
    def goBackToUsers(self):
        self.ids.body_screen_manager.transition = SlideTransition(direction = "right")
        self.ids.body_screen_manager.current = "users_list_screen"
    def goBackToPayScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "pay_screen"
    def unscheduleLoadingState(self):
        self.ids.loading_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.loading_screen_manager.current = "empty_screen"
        self.touch_allowed = True
        Clock.unschedule(self.makeRequest)
        Clock.unschedule(self.determineNextScreen)
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/transaction/", params = self.params).text)
            if response[0]  == 1:
                self.id = response[1]
                self.response = 1
        except:
            self.response = -2
            self.error_message = "Network connection failure"
    def determineNextScreen(self, seconds):
        if self.response == 1:
            button = MDFillRoundFlatButton(text = "Ok")
            self.unscheduleLoadingState()
            button.bind(on_release = self.close)
            self.callDialog("Feedback", self.response_message, button)
        elif self.response == -2:
            button = MDFillRoundFlatButton(text = "Ok")
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog("Feedback", self.error_message, button)
            button.bind(on_release = self.close)
        else:
            Clock.schedule_once(self.determineNextScreen, 0)
    def goToViewYourRequests(self):
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "my_money_requests"
    def callDoubleButtonForAmountRequestDialog(self, title, text, button_one, button_two):
        self.dialog = MDDialog(title = title, text = text, buttons = [button_one, button_two])
        button_one.bind(on_press = self.close)
        button_two.bind(on_press = self.continueRequest)
        self.dialog.open()
    def callDoubleButtonForAmountSendDialog(self, title, text, button_one, button_two):
        self.dialog = MDDialog(title = title, text = text, buttons = [button_one, button_two])
        button_one.bind(on_press = self.close)
        button_two.bind(on_press = self.continueSending)
        self.dialog.open()
    def callDialog(self, title, text, button):
        self.dialog = MDDialog(title = title, text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def continueSending(self, button):
        self.dialog.dismiss()
        self.touch_allowed = False
        self.response_message = "Money sent successfull"
        self.ids.loading_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.loading_screen_manager.current = "loading_screen"
        Clock.schedule_once(self.makeRequest, 0)
        Clock.schedule_once(self.determineNextScreen, 3)
    def continueRequest(self, button):
        self.dialog.dismiss()
        self.touch_allowed = False
        self.response_message = "Request made successfull"
        self.ids.loading_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.loading_screen_manager.current = "loading_screen"
        Clock.schedule_once(self.makeRequest, 0)
        Clock.schedule_once(self.determineNextScreen, 3)
    def close(self, button):
        self.dialog.dismiss()
class TestApp(MDApp):
    def build(self):
        root = WhoToPayScreen()
        return root
if __name__ == "__main__":
    TestApp().run()