
# kivymd_ui.py
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager, MDScreen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView

KV = '''
MDScreenManager:
    MenuScreen:
    PaymentScreen:
    TransactionScreen:

<MenuScreen>:
    name: 'menu'

    MDTopAppBar:
        title: 'Digital Pay'
        left_action_items: [['menu', lambda x: None]]
        elevation: 10

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        MDLabel:
            text: 'Welcome to Digital Pay'
            halign: 'center'
            font_style: 'H4'
        MDIconButton:
            icon: 'credit-card'
            user_font_size: '64sp'
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'Make a Payment'
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'payment'
        MDRaisedButton:
            text: 'View Transactions'
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'transactions'

<PaymentScreen>:
    name: 'payment'

    MDTopAppBar:
        title: 'Make a Payment'
        left_action_items: [['arrow-left', lambda x: root.manager.current = 'menu']]
        elevation: 10

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDTextField:
            id: recipient
            hint_text: 'Recipient Username'
            icon_right: 'account'

        MDTextField:
            id: amount
            hint_text: 'Amount'
            icon_right: 'currency-usd'
            input_filter: 'float'

        MDRaisedButton:
            text: 'Send Money'
            pos_hint: {'center_x': 0.5}
            on_release: app.send_money()

<TransactionScreen>:
    name: 'transactions'

    MDTopAppBar:
        title: 'Transaction History'
        left_action_items: [['arrow-left', lambda x: root.manager.current = 'menu']]
        elevation: 10

    ScrollView:
        MDBoxLayout:
            id: transaction_list
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(10)
            adaptive_height: True
'''

class MenuScreen(MDScreen):
    pass

class PaymentScreen(MDScreen):
    pass

class TransactionScreen(MDScreen):
    pass

class DigitalPaymentApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def send_money(self):
        recipient = self.root.get_screen('payment').ids.recipient.text
        amount = self.root.get_screen('payment').ids.amount.text
        if recipient and amount:
            self.root.get_screen('transactions').ids.transaction_list.add_widget(
                MDCard(
                    orientation='vertical',
                    padding=10,
                    size_hint=(1, None),
                    height='100dp',
                    md_bg_color=self.theme_cls.primary_light,
                    line_color=(0, 0, 0, 0.2),
                    ripple_behavior=True,
                    children=[
                        MDLabel(
                            text=f'Sent {amount} to {recipient}',
                            halign='center',
                            theme_text_color='Primary'
                        )
                    ]
                )
            )
            self.root.get_screen('payment').ids.recipient.text = ''
            self.root.get_screen('payment').ids.amount.text = ''
            self.root.current = 'transactions'

if __name__ == '__main__':
    DigitalPaymentApp().run()
