from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
from load import LoadingScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<TransactionBarBox>:
    size_hint_y:None
    height:"70dp"
    radius:[30, 30, 30, 30]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    padding:"10dp", "10dp"
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
                bold:True
                text_size:self.size
                halign:"left"
                valign:"middle"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:date_and_time
                text:"01/Jan/2000"
                text_size:self.size
                halign:"left"
                color:[140/float(255), 140/float(255), 140/float(255), 1]
                valign:"middle"
    MDBoxLayout:
        size_hint_x:None
        width:transaction_amount_label.width
        MDLabel:
            id:transaction_amount_label
            text:"+R1200"
            bold:True
            text_size:None, self.height
            size_hint:None, 1
            width:self.texture_size[0]
            color:[0/float(255), 154/float(255), 255/float(255), 1]
<WalletScreen>:
    name:"wallet_screen"
    id:wallet_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"5dp", "0dp"
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            radius:[20, 20, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackHome()
            MDLabel:
                text:"Wallet"
                font_size:"23dp"
                text_size:self.size
                halign:"left"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            orientation:"vertical"
            radius:[0, 0, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDBoxLayout:
                size_hint_y:None
                height:"140dp"
                orientation:"vertical"
                MDBoxLayout:
                    size_hint_y:None
                    height:"40dp"
                    padding:"5dp", "0dp"
                    MDIconButton:
                        size_hint:None, None
                        size:"40dp", "40dp"
                        icon:"wallet"
                        user_font_size:"30dp"
                        theme_text_color:"Custom"
                        text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                        pos_hint:{"center_y":.5}
                    MDLabel:
                        text:"Your balance (R120)"
                        text_size:self.size
                        halign:"left"
                        valign:"middle"
                        color:[255/float(255), 255/float(255), 255/float(255), 1]
                MDBoxLayout:
                    spacing:10
                    size_hint_y:None
                    height:"100dp"
                    padding:5, 0, 0, 10
                    Widget:
                    CashOutTab:
                        id:cash_out_tab
                        root:wallet_screen
                        orientation:"vertical"
                        size_hint_x:None
                        width:"140dp"
                        radius:[20, 20, 20, 20]
                        md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
                        MDBoxLayout:
                            Widget:
                            MDIconButton:
                                id:cash_out_icon_button
                                size_hint:None, None
                                size:"50dp", "50dp"
                                user_font_size:"40dp"
                                theme_text_color:"Custom"
                                text_color:[0/float(255), 255/float(255), 154/float(255), 1]
                                icon:"sticker-minus"
                                pos_hint:{"center_x":.5, "center_y":.5}
                            Widget:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"30dp"
                            MDLabel:
                                id:cash_out_label
                                text:"Cash out"
                                bold:True
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                    CashInTab:
                        id:cash_in_tab
                        root:wallet_screen
                        orientation:"vertical"
                        size_hint_x:None
                        width:"140dp"
                        radius:[20, 20, 20, 20]
                        md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
                        MDBoxLayout:
                            Widget:
                            MDIconButton:
                                id:cash_in_icon_button
                                size_hint:None, None
                                size:"50dp", "50dp"
                                user_font_size:"40dp"
                                theme_text_color:"Custom"
                                text_color:[72/float(255), 61/float(255), 139/float(255), 1]
                                icon:"sticker-plus"
                                pos_hint:{"center_x":.5, "center_y":.5}
                            Widget:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"30dp"
                            MDLabel:
                                id:cash_in_label
                                text:"Cash in"
                                bold:True
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                    Widget:
            MDBoxLayout:
                radius:[20, 20, 0, 0]
                padding:5, 10, 5, 0
                md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                ScreenManager:
                    id:sub_screen_manager
                    MDScreen:
                        name:"cash_out_screen"
                        MDBoxLayout:
                            ScrollView:
                                size_hint:None, None
                                size:self.parent.size
                                bar_width:0
                                CashOutLayout:
                    MDScreen:
                        name:"cash_in_screen"
                        MDBoxLayout:
                            ScrollView:
                                size_hint:None, None
                                size:self.parent.size
                                width:0
                                CashInLayout:
""")
class TransactionBarBox(MDBoxLayout):
    pass
class CashOutTab(TouchBox):
    def respondToTouch(self):
        print("Hello Cash Out Tab")
        self.root.ids.cash_out_tab.md_bg_color = [0/float(255), 0/float(255), 0/float(255), 1]
        self.root.ids.cash_out_label.color = [1, 1, 1, 1]
        self.root.ids.cash_in_tab.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
        self.root.ids.cash_in_label.color = [1, 1, 1, 1]
        self.root.ids.cash_out_icon_button.text_color = [0, 255/float(255), 154/float(255), 1]
        self.root.ids.cash_in_icon_button.text_color = [72/float(255), 61/float(255), 139/float(255), 1]
        self.root.ids.sub_screen_manager.transition = SlideTransition(direction = "left")
        self.root.ids.sub_screen_manager.current = "cash_out_screen"
class CashInTab(TouchBox):
    def respondToTouch(self):
        print("Hello Cash In Tab")
        self.root.ids.cash_out_tab.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
        self.root.ids.cash_out_label.color = [1, 1, 1, 1]
        self.root.ids.cash_in_tab.md_bg_color = [0/float(255), 0/float(255), 0/float(255), 1]
        self.root.ids.cash_in_label.color = [1, 1, 1, 1]
        self.root.ids.cash_out_icon_button.text_color = [72/float(255), 61/float(255), 139/float(255), 1]
        self.root.ids.cash_in_icon_button.text_color = [0/float(255), 255/float(255), 154/float(255), 1]
        self.root.ids.sub_screen_manager.transition = SlideTransition(direction = "right")
        self.root.ids.sub_screen_manager.current = "cash_in_screen"
class CashOutLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.padding = "5dp", "10dp"
        self.cash_out = [["goodwill@gmail.com", "10/Dec/2020 time 10:40", "4000"]]
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addMoneyOut()
    def addMoneyOut(self):
        for user in self.cash_out *10:
            transaction_bar_box = TransactionBarBox()
            transaction_bar_box.ids.name_first_letter.text = user[0][0].upper()
            transaction_bar_box.ids.email_address.text = user[0]
            transaction_bar_box.ids.date_and_time.text = user[1]
            transaction_bar_box.ids.transaction_amount_label.color = [255/float(255), 69/float(255), 0/float(255), 1]
            transaction_bar_box.ids.transaction_amount_label.text = "-R" + user[2]
            self.add_widget(transaction_bar_box)
class CashInLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.padding = "5dp", "10dp"
        self.cash_in = [["sakhi@gmail.com", "10/Dec/2020 time 10:40", "4000"]]
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addMoneyIn()
    def addMoneyIn(self):
        for user in self.cash_in*10:
            transaction_bar_box = TransactionBarBox()
            transaction_bar_box.ids.name_first_letter.text = user[0][0].upper()
            transaction_bar_box.ids.email_address.text = user[0]
            transaction_bar_box.ids.date_and_time.text = user[1]
            transaction_bar_box.ids.transaction_amount_label.text = "+R" + user[2]
            self.add_widget(transaction_bar_box)
class WalletScreen(MDScreen):
    def goBackHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
class Test(MDApp):
    def build(self):
        root = WalletScreen()
        return root
if __name__ == "__main__":
    Test().run()