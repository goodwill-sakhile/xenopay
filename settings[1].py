from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from credentials_checker import *
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
ui = Builder.load_string("""
<LoadingBox>:
    size_hint:None, None
    size:"50dp", "50dp"
    Image:
        source:"load.gif"
        center:self.parent.center
        size:40, 40
        allow_stretch:True
        anim_delay:-1
        anim_loop:10000000000000000000000000
        anim_delay:0.01
<ChangeEmailBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"email"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"Change Email"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<ChangePasswordBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"key-variant"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"Change Password"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<AboutBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"information"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"About"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<ReactionBarBox>:
    orientation:"vertical"
    MDBoxLayout:
        MDLabel:
            text:"How was your user experiance"
            text_size:self.size
            halign:"center"
            valign:"middle"
    MDBoxLayout:
        spacing:5
        BoxLayout:
        MDIconButton:
            id:heart_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"heart-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithHeart()
        MDIconButton:
            id:thumb_up_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"thumb-up-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithThumbUp()
        MDIconButton:
            id:happy_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-happy-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithHappyFace()
        MDIconButton:
            id:cool_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-cool-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithCoolFace()
        MDIconButton:
            id:frown_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-frown-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithFrownFace()
        BoxLayout:
<SettingsScreen>:
    id:settings_screen_object
    name:"settings_screen"
    md_bg_color:[0, 0, 0, 1]
    MDBoxLayout:
        orientation:"vertical"
        padding:"5dp", "5dp"
        spacing:5
        md_bg_color:[0, 0, 0, 1]
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            size_hint_y:None
            height:"130dp"
            orientation:"vertical"
            radius:[20, 20, 20, 20]
            MDBoxLayout:
                MDIconButton:
                    size_hint:None, None
                    size:"50dp", "50dp"
                    user_font_size:"30dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    icon:"arrow-left-thick"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    on_release:root.goBackToHome()
                MDLabel:
                    text:"Settings"
                    font_size:"25dp"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDBoxLayout:
                    size_hint:None, None
                    size:"50dp", "50dp"
            MDBoxLayout:
                size_hint_y:None
                height:"80dp"
                padding:"5dp", "0dp"
                MDTextField:
                    hint_text:"---Feedback---"
                    icon_right:"send"
                    mode:"fill"
                    radius:[20, 20, 20, 20]
                    pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            ScreenManager:
                id:settings_body_screen_manager
                Screen:
                    name:"menu_screen"
                    MDBoxLayout:
                        screen_manager:settings_body_screen_manager
                        spacing:10
                        padding:"10dp", "10dp", "10dp", "10dp"
                        orientation:"vertical"
                        ChangeEmailBarBox:
                        ChangePasswordBarBox:
                        AboutBarBox:                       
                Screen:
                    name:"change_email_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                user_font_size:"30dp"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                icon:"menu"
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"Change Email"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            root:settings_screen_object
                            padding:"10dp", "0dp"
                            spacing:5
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:new_email_object
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--New Email"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:confirm_email_object
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Confirm Email"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            ChangeEmailContinueButton:
                                id:change_email_button
                                root:settings_screen_object
                                size_hint_y:None
                                height:"50dp"
                                radius:[30, 30, 30, 30]
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                MDLabel:
                                    text:"Continue"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                            Widget:
                Screen:
                    name:"change_password_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                user_font_size:"30dp"
                                icon:"menu"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"Change Password"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            root:settings_screen_object
                            padding:"10dp", "0dp"
                            spacing:5
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:old_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Old Password"
                                    password:True
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:new_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    password:True
                                    hint_text:"--New Password"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:confirm_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Verify Password"
                                    password:True
                            ChangePasswordContinueButton:
                                id:change_password_button
                                root:settings_screen_object
                                size_hint_y:None
                                height:"50dp"
                                radius:[30, 30, 30, 30]
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                MDLabel:
                                    text:"Continue"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                            Widget:
                Screen:
                    name:"about_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                icon:"menu"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                user_font_size:"30dp"
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"About"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                Widget:
                                MDIconButton:
                                    size_hint:None, None
                                    size:"70dp", "70dp"
                                    icon:"information"
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    user_font_size:"60dp"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                Widget:
                            MDBoxLayout:
                                size_hint_y:None
                                height:about_label.height
                                Label:
                                    text:"Xenopay version 1.0.0 for android is a payment application that works with different retailers to facilitate payments and money deposits"
                                    id:about_label
                                    text_size:self.width, None
                                    size_hint:1, None
                                    halign:"center"
                                    valign:"middle"
                                    height:self.texture_size[1]
                                    color:[1, 1, 1, 1]
                            MDBoxLayout:
                            MDBoxLayout:
                                size_hint_y:None
                                height:"30dp"
                                MDLabel:
                                    color:[120/float(255), 120/float(255), 120/float(255), 1]
                                    text:"Copyright@2022 Xenopay all right reserved"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
""")
class LoadingBox(MDBoxLayout):
    pass
class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.touch = True
        self.params = {}
        self.failure_message = ""
        self.success_message = ""
    def changeEmailaddLoading(self, seconds):
        self.touch = False
        self.ids.change_email_button.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.ids.change_email_button.text = "Loading..."
        self.ids.change_email_button.add_widget(LoadingBox())
    def changePasswordaddLoading(self, seconds):
        self.touch = False
        self.ids.change_password_button.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.ids.change_password_button.text = "Loading..."
        self.ids.change_password_button.add_widget(LoadingBox())
    def goBackToSettingsMenu(self):
        self.ids.settings_body_screen_manager.transition = SlideTransition(direction ="right")
        self.ids.settings_body_screen_manager.current = "menu_screen"
    def goBackToHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
    def unscheduleLoadingState(self):
        Clock.unschedule(self.makeRequest)
        Clock.unschedule(self.determineNextScreen)
        if self.ids.settings_body_screen_manager.current == "change_email_screen":
            print("Current screen is Emaillll.......")
            Clock.unschedule(self.changeEmailaddLoading)
            _object = self.ids.change_email_button
        else:
            Clock.unschedule(self.changePasswordaddLoading)
            _object = self.ids.change_password_button
        _object.text = "Continue"
        _object.remove_widget(_object.children[0])
        _object.md_bg_color = [0, 154/float(255), 255/float(255), 1]
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/gateway/changePassword/", params = self.params).text)
            if response[0]  == 1:
                self.id = response[1]
                self.response = 1
            else:
                self.response = 0
        except:
            self.response = -2
            self.error_message = "Network connection failure"
    def determineNextScreen(self, seconds):
        if self.response == 1:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.success_message, button)
            button.bind(on_release = self.close)
        elif self.response == 0:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.error_message, button)
            button.bind(on_release = self.close)
        elif self.response == -2:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.error_message, button)
            button.bind(on_release = self.close)
        else:
            Clock.schedule_once(self.determineNextScreen, 0)
    def callDialog(self, text, button):
        self.dialog = MDDialog(title = "Settings change", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
    def respondToTouch(self):
	    pass
class ChangePasswordContinueButton(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.touch = True
    def checkPasswordChangeCredentials(self, old_password, password_one, password_two):
        if not (old_password and password_one and password_two):
            return 0
        else:
            return 1
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Change password error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        print("Dismiss button pressed")
        self.dialog.dismiss()
    def respondToTouch(self):
	    old_password = self.parent.root.ids.old_password.text
	    new_password = self.parent.root.ids.new_password.text
	    confirm_password = self.parent.root.ids.confirm_password.text
	    print(old_password, new_password, confirm_password)
	    if not self.checkPasswordChangeCredentials(old_password, new_password, confirm_password):
	        self.callDialog("Fill all text fields correctly!")
	    else:
	        if not (new_password == confirm_password):
	            self.callDialog("New passwords don't match!")
	        elif self.touch:
	            self.root.params = {"old_password":old_password, "new_password":new_password}
	            self.root.failure_message = "Failure : couldnt change password!"
	            self.root.success_message = "Success: password changed"
	            Clock.schedule_once(self.root.changePasswordaddLoading, 0)
	            Clock.schedule_once(self.root.makeRequest, 0)
	            Clock.schedule_once(self.root.determineNextScreen, 2)
class ChangeEmailContinueButton(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.touch = True
    def checkEmailChangeCredentials(self, email_one, email_two):
        if not (email_one and email_two):
            return 0
        else:
            return 1
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Change password error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        print("Dismiss button pressed")
        self.dialog.dismiss()
    def respondToTouch(self):
        new_email = self.parent.root.ids.new_email_object.text
        confirm_email = self.parent.root.ids.confirm_email_object.text
        print(new_email, confirm_email)
        if not self.checkEmailChangeCredentials(new_email, confirm_email):
	        self.callDialog("Fill all text fields correctly!")
        else:
            n_email_checker = checkEmailQualification(new_email)
            c_email_checker = checkEmailQualification(confirm_email)
            if not (n_email_checker and c_email_checker):
                self.callDialog("Wrong email format!")
            elif not (new_email == confirm_email):
                self.callDialog("Emails don't match!")
            elif self.touch:
                self.root.params = {"new_email":new_email, "confirm_email":confirm_email}
                self.root.failure_message = "Failure : couldnt change email!"
                self.root.success_message = "Success: email changed"
                Clock.schedule_once(self.root.changeEmailaddLoading, 0)
                Clock.schedule_once(self.root.makeRequest, 0)
                Clock.schedule_once(self.root.determineNextScreen, 2)
class ChangeEmailBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "change_email_screen"
class ChangePasswordBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "change_password_screen"
class AboutBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "about_screen"
class ReactionBarBox(MDBoxLayout):
    def respondToTouch(self):
        pass
    def reactWithHeart(self):
        self.ids.heart_button_object.icon = "heart"
    def reactWithThumbUp(self):
        self.ids.thumb_up_button_object.icon = "thumb-up"
    def reactWithHappyFace(self):
        self.ids.happy_button_object.icon = "emoticon-happy"
    def reactWithCoolFace(self):
        self.ids.cool_button_object.icon = "emoticon-cool"
    def reactWithFrownFace(self):
        self.ids.frown_button_object.icon = "emoticon-frown"