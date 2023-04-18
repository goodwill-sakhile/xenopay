from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from link import LinkUserScreen
from touch import TouchBox
from settings import SettingsScreen
from kivy.lang import Builder
from wallet import WalletScreen
from pay import PayScreen
import _thread as thread
from load import LoadingScreen
from market_view import MarketsViewScreen
from money_requests import MoneyRequestsScreen
from kivy.clock import Clock
import time
ui = Builder.load_string("""
<BasicTouchBox>:
    radius:[20, 20, 20, 20]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    orientation:"vertical"
    text:""
    icon:""
    MDBoxLayout:
        Widget:
        MDIconButton:
            id:icon_button
            size_hint:None, None
            size:"60dp", "60dp"
            user_font_size:"40dp"
            icon:root.icon
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            pos_hint:{"center_x":.5, "center_y":.5}
        Widget:
    MDBoxLayout:
        size_hint_y:None
        height:"50dp"
        MDLabel:
            text:root.text
            text_size:self.size
            halign:"center"
            valign:"middle"
            font_size:"18dp"
            color:[1, 1, 1, 1]
<MenuScreen>:
    name:"menu_screen"
    id:menu_screen
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            MDIconButton:
                icon:"menu"
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                pos_hint:{"center_y":.5}
        MDBoxLayout:
            MDGridLayout:
                root:menu_screen
                spacing:10
                cols:2
                rows:3
                WalletTouchBox:
                    id:wallet_button
                    icon:"wallet"
                    text:"Wallet"
                LinkUserTouchBox:
                    id:link_user_button
                    icon:"link-variant-plus"
                    text:"Link user"
                PayTouchBox:
                    id:pay_button
                    icon:"offer"
                    text:"Pay"
                RequestsTouchBox:
                    id:request_button
                    icon:"motion"
                    text:"Requests"
                MarketsTouchBox:
                    id:market_button
                    icon:"chart-timeline-variant"
                    text:"Markets"
                SettingsTouchBox:
                    id:settings_button
                    icon:"cog"
                    text:"Settings"
<HomeLoadScreen>:
    name:"home_load_screen"
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
<HomeScreen>:
    id:home_screen_object
    name:"home_screen"
    MDBoxLayout:
        md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
        orientation:"vertical"
        padding:"5dp", "5dp"
        spacing:0
        MDBoxLayout:
            radius:[20, 20, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            size_hint_y:None
            padding:"10dp", "0dp"
            height:"80dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"arrow-left-thick"
                user_font_size:"30dp"
                pos_hint:{"center_y":.5}
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                on_press:root.logOut()
            MDLabel:
                text:"Xenopay"
                font_size:"24dp"
                color:[1, 1, 1, 1]
                text_size:self.size
                halign:"left"
                valign:"middle"
        MDBoxLayout:
            orientation:"vertical"
            radius:[0, 0, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            padding:10
            MDBoxLayout:
                ScreenManager:
                    id:body_screen_manager
                    home_screen:home_screen_object
                    MenuScreen:
                        id:menu_screen
                        root:home_screen_object
                        FloatLayout:
                            pos:self.parent.pos
                            size:self.parent.size
                            MDBoxLayout:
                                pos:self.parent.pos
                                ScreenManager:
                                    id:menu_sub_screen_manager
                                    MDScreen:
                                        name:"empty_screen"
                                    HomeLoadScreen:
                    LinkUserScreen:
""")
class HomeLoadScreen(MDScreen):
    #home load screen 
    pass
class BasicTouchBox(TouchBox):
    def addLoadingScreen(self):
        #add loading screen
        self.parent.root.root.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.root.ids.menu_sub_screen_manager.current = "home_load_screen"
    def changeIconColor(self, color =[1, 1, 1, 1]):
        #change color of icon
        self.ids.icon_button.text_color = color
    def checkScreenExistence(self, screen_name):
        #check if main screen manager contains screen x
        if not self.parent.root.root.parent.has_screen(screen_name):
            return False
        return True
class WalletTouchBox(BasicTouchBox):
    def unscheduleLoadingState(self):
        Clock.unschedule(self.goToWallet)
        #stop loading and switch from loading screen to empty screen
        self.parent.root.root.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.root.ids.menu_sub_screen_manager.current = "empty_screen"
        self.parent.root.root.loading = False
    def goToLoading(self):
        #swith top loading top screen
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "loading_screen"
    def respondToTouch(self):
        #when touched respond by going to wallet_screen
        if not self.parent.root.root.loading:
            self.parent.root.root.loading = True
            screen_exist = self.checkScreenExistence("wallet_screen")
            self.changeIconColor([20/float(255), 20/float(255), 20/float(255), 1])
            if not screen_exist:
                self.addLoadingScreen()
                Clock.schedule_once(self.goToWallet, 1)
            else:
                self.main = self.parent.root.parent.home_screen.parent
                self.main.transition = SlideTransition(direction = "left")
                self.main.current = "wallet_screen"
                self.ids.icon_button.text_color = [1, 1, 1, 1]
    def goToWallet(self, seconds):
        #call WalletScreen and add it to main screen manager
        self.main = self.parent.root.parent.home_screen.parent
        if not self.main.has_screen("wallet_screen"):
            wallet_screen = WalletScreen()
            self.main.add_widget(wallet_screen)
        self.main.transition = SlideTransition(direction = "left")
        self.main.current = "wallet_screen"
        self.unscheduleLoadingState()
        self.ids.icon_button.text_color = [1, 1, 1, 1]
class LinkUserTouchBox(BasicTouchBox):
    def respondToTouch(self):
        #when touched respond by going to link_user_screen
        self.parent.root.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.current = "link_user_screen"
class PayTouchBox(BasicTouchBox):
    def unscheduleLoadingState(self):
        #unschedule addPayScreen function loading thread
        Clock.unschedule(self.addPayScreen)
    def addPayScreen(self, seconds):
        #add pay_screen concurrently by loading
        if not self.parent.root.parent.home_screen.parent.has_screen("pay_screen"):
            pay_screen = PayScreen()
            self.parent.root.parent.home_screen.parent.add_widget(pay_screen)
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "pay_screen"
        self.parent.root.root.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.root.ids.menu_sub_screen_manager.current = "empty_screen"
        if self.parent.root.root.loading:
            self.parent.root.root.loading = False
            self.unscheduleLoadingState()
        self.ids.icon_button.text_color = [1, 1, 1, 1]
    def respondToTouch(self):
        #when touched check if main screen manager top layer is on loading
        #if it not on loading it schedule addPayScreen function addition thread
        if not self.parent.root.root.loading:
            self.parent.root.root.loading = True
            self.parent.root.root.addLoadingScreen()
            self.changeIconColor([20/float(255), 20/float(255), 20/float(255), 1])
            Clock.schedule_once(self.addPayScreen, 1)
            #self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
            #self.parent.root.parent.home_screen.parent.current = "pay_screen"
class RequestsTouchBox(BasicTouchBox):
    def unscheduleLoadingState(self):
        Clock.unschedule(self.addMoneyRequestScreen)
        self.parent.root.root.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.root.ids.menu_sub_screen_manager.current = "empty_screen"
        self.parent.root.root.loading = False
    def respondToTouch(self):
        if not self.parent.root.root.loading:
            self.parent.root.root.loading = True
            self.addLoadingScreen()
            self.changeIconColor([20/float(255), 20/float(255), 20/float(255), 1])
            Clock.schedule_once(self.addMoneyRequestScreen, 1)
    def addMoneyRequestScreen(self, seconds):
        if not self.parent.root.parent.home_screen.parent.has_screen("money_requests_screen"):
            money_request_screen = MoneyRequestsScreen()
            self.parent.root.parent.home_screen.parent.add_widget(money_request_screen)
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "money_requests_screen"
        self.unscheduleLoadingState()
        self.ids.icon_button.text_color = [1, 1, 1, 1]
class MarketsTouchBox(BasicTouchBox):
    def unscheduleLoadingState(self):
        Clock.unschedule(self.addMarketsScreen)
    def addMarketsScreen(self, seconds):
        if not self.parent.root.parent.home_screen.parent.has_screen("market_view_screen"):
            market_view_screen  = MarketsViewScreen()
            thread.start_new_thread(market_view_screen.plotAllGraphs, ("BTC-USD", "DOGE-USD", "ETH-USD"))
            thread.start_new_thread(market_view_screen.plotAllGraphs, ("USDZAR=X", "GBPZAR=X", "EURZAR=X"))
            self.parent.root.parent.home_screen.parent.add_widget(market_view_screen)
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "market_view_screen"
        self.parent.root.root.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.root.ids.menu_sub_screen_manager.current = "empty_screen"
        if self.parent.root.root.loading:
            self.parent.root.root.loading = False
            self.unscheduleLoadingState()
        self.ids.icon_button.text_color = [1, 1, 1, 1]
    def respondToTouch(self):
        if not self.parent.root.root.loading:
            self.parent.root.root.loading = True
            self.parent.root.root.addLoadingScreen()
            self.changeIconColor([20/float(255), 20/float(255), 20/float(255), 1])
            Clock.schedule_once(self.addMarketsScreen, 1)
            #market_view_screen = self.parent.root.parent.home_screen.parent.ids.market_view_screen
            #market_view_screen.ids.body_screen_manager.transition = NoTransition()
            #market_view_screen.ids.body_screen_manager.current = "crypto_market_screen"
            #market_view_screen.ids.screen_title.text = "Crypto Markets View"
        #
class SettingsTouchBox(BasicTouchBox):
    def respondToTouch(self):
        if not self.parent.root.root.loading:
            self.parent.root.root.loading = True
            self.parent.root.root.addLoadingScreen()
            self.changeIconColor([20/float(255), 20/float(255), 20/float(255), 1])
            Clock.schedule_once(self.parent.root.root.goToSettings, 1)
            #market_view_screen  = MarketsViewScreen()
            #self.parent.root.parent.home_screen.parent.add_widget(market_view_screen)
            #market_view_screen = self.parent.root.parent.home_screen.parent.ids.market_view_screen
            #market_view_screen.ids.body_screen_manager.transition = NoTransition()
            #market_view_screen.ids.body_screen_manager.current = "currency_market_screen"
            #market_view_screen.ids.screen_title.text = "Exchange Market View"
            #self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
            #self.parent.root.parent.home_screen.parent.current = "market_view_screen"
            #thread.start_new_thread(market_view_screen.plotAllGraphs, ("USDZAR=X", "GBPZAR=X", "EURZAR=X"))
class MenuScreen(MDScreen):
    pass
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._parent = None
        self.loading = False
        self.id = ""
    def moveToLoadingScreen(self, seconds):
        if not self.parent.has_screen("loading_screen"):
            loading_screen = LoadingScreen()
            self.parent.add_widget(loading_screen)
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "loading_screen"
    def logOut(self):
        print("Gateway screen :", self.parent.ids.gate_way_screen.ids.gateway_sub_screen_manager)
        self.parent.ids.gate_way_screen.ids.gateway_sub_screen_manager.transition = NoTransition()
        self.parent.ids.gate_way_screen.ids.gateway_sub_screen_manager.current = "login_screen"
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "gateway_screen"
    def addLoadingScreen(self):
        self.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.menu_sub_screen_manager.current = "home_load_screen"
    def unscheduleLoadingState(self):
        Clock.unschedule(self.goToSettings)
    def goToSettings(self, seconds):
        if not self.loading:
            self.loading = True
            self.addLoadingScreen()
        if not self.parent.has_screen("settings_screen"):
            settings_screen = SettingsScreen()
            self.parent.add_widget(settings_screen)
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "settings_screen"
        if self.loading:
            self.loading = False
            self.unscheduleLoadingState()
        self.ids.menu_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.menu_sub_screen_manager.current = "empty_screen"
        self.ids.menu_screen.ids.settings_button.ids.icon_button.text_color = [1, 1, 1, 1]
class Test(MDApp):
    def build(self):
        root = HomeScreen()
        return root
if __name__ == "__main__":
    Test().run()