from atexit import register
from code import interact
from gc import callbacks
import imp
from msilib.schema import Icon
import random
from operator import iconcat
from unicodedata import name
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivy.uix.checkbox import CheckBox
from kivy.storage.jsonstore import JsonStore
import json
import requests
from kivymd.uix.picker import MDDatePicker, MDThemePicker
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivy_garden.mapview import MapView
from kivymd.uix.bottomsheet import MDCustomBottomSheet, MDGridBottomSheet
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.core.window import Window
import webbrowser


username_helper = """

Screen: 
    ScreenManager:
        WelcomeScreen:
        LoginScreen:
        RegisterScreen:
        HomeScreen:
        MapScreen:
        DepositScreen:
        InterestScreen:
        TransferScreen:
        CardScreen:
        SettingScreen:

<WelcomeScreen>:
    name: 'welcome'
    FloatLayout:
        Image:
            source: 'bank_logo_ed.png'
            size_hint: None, None
            pos_hint: {'center_x':0.5, 'center_y':0.7}
            size: '300dp', '300dp'
        MDLabel:
            text: 'Welcome to your virtual bank'
            font_style: 'H5'
            halign: 'center'
            pos_hint: {'center_y': 0.4}
        MDRaisedButton:
            text: 'Get Started'
            font_size: '20dp'
            radius: '5dp'
            pos_hint: {'center_x':0.5, 'center_y': 0.3}
            on_press: root.manager.current = 'register'
        MDRectangleFlatButton:
            text: 'Already have an account'
            pos_hint: {'center_x':0.5, 'center_y': 0.22}
            on_press: root.manager.current = 'login'

<LoginScreen>:
    name: 'login'
    MDTextField:
        id: log_email
        hint_text : "Email"
        helper_text : ""
        helper_text_mode : "on_focus"
        icon_right : "email"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y':0.6}
        size_hint_x : None
        width : 250
    
    MDTextField:
        id: log_pass
        hint_text : "Password"
        helper_text : ""
        helper_text_mode : "on_focus"
        icon_right : "key"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y':0.48}
        size_hint_x : None
        width : 250
    
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.35, 'center_y':0.3}
        on_press: 
            root.login_info()
            # app.username_changer()

    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {'center_x':0.65, 'center_y':0.3}
        on_press: root.manager.current = 'register'

    MDLabel:
        text: 'Login'
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'Button'
        font_size: '50dp'


<RegisterScreen>:
    name: 'register'

    MDCard:
        orientation: "vertical"
        size_hint: None, None
        size: 300, 500
        radius: '10dp'
        elevation: 10
        padding: 25
        spacing: 25
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: 'registration'
            halign: 'center'
            pos_hint: {'center_y':0.95}
            font_style: 'Button'
            font_size: '35dp'
        
        Widget:
            size_hint_y: None
            height: 230

        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            MDTextField:
                id: reg_name_first
                hint_text : "First Name"
                icon_right : "account"
                icon_right_color : app.theme_cls.primary_color
                size_hint_x : None
                width : 250
            MDTextField:
                id: reg_name_last
                hint_text : "Last Name"
                icon_right : "account"
                icon_right_color : app.theme_cls.primary_color
                size_hint_x : None
                width : 250
            MDTextField:
                id: reg_name_user
                hint_text : "Username"
                helper_text : ""
                helper_text_mode : "on_focus"
                icon_right : "account"
                icon_right_color : app.theme_cls.primary_color
                # pos_hint : {'center_x':0.5, 'center_y':0.53}
                size_hint_x : None
                width : 250
            MDTextField:
                id: reg_email
                hint_text : "Email"
                icon_right : "email"
                icon_right_color : app.theme_cls.primary_color
                # pos_hint : {'center_x':0.5, 'center_y':0.65}
                size_hint_x : None
                width : 250
            MDTextField:
                id: reg_pass
                hint_text : "Password"
                helper_text : "Maximum length 8 characters"
                max_text_length: 8
                helper_text_mode : "on_focus"
                icon_right : "key"
                icon_right_color : app.theme_cls.primary_color
                # pos_hint : {'center_x':0.5, 'center_y':0.4}
                size_hint_x : None
                width : 250

        BoxLayout:
            orientation: 'horizontal'
            spacing: 25
            pos_hint: {'center_x':0.5}
            MDRectangleFlatButton:
                text: 'Login'
                on_press: root.manager.current = 'login'
            MDRaisedButton:
                text: 'CREATE ACCOUNT'
                on_press: root.register_info()


<HomeScreen>:
    name: 'home'
    id: home

    MDCard:
        orientation: 'vertical'
        size_hint: None, None
        padding: '10dp'
        size: root.width - (dp(30)), "170dp"
        radius: '10dp'
        pos_hint: {"center_x": .5, "center_y": 0.7}

        MDLabel:
            text: 'Your Balance'
            font_style: 'H4'
            pos_hint: {'center_y':0.8}
        MDSeparator:
            height: '5dp'
            width: root.width - (dp(40))
        MDLabel:
            id: display_amount
            text: '100000'
            font_style: 'H5'
            pos_hint: {'center_y':0.2}

    MDCard:
        size_hint: None, None
        padding: 0
        size: root.width - (dp(30)), "300dp"
        radius: '10dp'
        md_bg_color: (180/255, 197/255, 133/255, 0)
        pos_hint: {"center_x": .5, "center_y": 0.27}
        GridLayout:
            cols: 2
            rows: 2
            spacing: '10dp'
            
            MDCard:
                orientation: "vertical"
                size: '200dp', '200dp'
                radius: '10dp'
                md_bg_color: (60/255, 179/255, 113/255, 1)
                on_press: root.manager.current = 'deposit'
                MDLabel:
                    text: 'Deposit'
                    font_style: 'H6'
                    halign: 'center'
            MDCard:
                orientation: 'vertical'
                size: '200dp', '200dp'
                radius: '10dp'
                md_bg_color: (130/255, 182/255, 210/255, 1)
                on_press: root.manager.current = 'transfer'
                MDLabel:
                    text: 'Transfer'
                    font_style: 'H6'
                    halign: 'center'
            MDCard:
                orientation: 'vertical'
                size: '200dp', '200dp'
                radius: '10dp'
                md_bg_color: (230/255, 191/255, 73/255, 1)
                on_press: root.manager.current = 'vir_card'
                MDLabel:
                    text: 'Virtual Card'
                    font_style: 'H6'
                    halign: 'center'
            MDCard:
                orientation: 'vertical'
                size: '200dp', '200dp'
                radius: '10dp'
                md_bg_color: (239/255, 134/255, 119/255, 1)
                on_press: app.support_open()
                MDLabel:
                    text: 'Support'
                    font_style: 'H6'
                    halign: 'center'

    MDToolbar:
        pos_hint: {"top":1}
        title: "Dashboard"
        elevation: 20
        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
        # right_action_items: [['link', lambda x: app.show_bottom_sheet()]]

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
            MDCard:
                size_hint: None, None
                size: nav_drawer.width - (dp(20)), '200dp'
                md_bg_color: (1,1,1,0)
                elevation: 0
                BoxLayout:
                    orientation: 'vertical'
                    Image:
                        source: 'acc1.webp'
                        size_hint: None, None
                        size: '150dp', '150dp'
                        pos_hint: {'center_x': 0.5}
                    MDLabel:
                        id: home_username
                        text: 'username'
                        font_style: 'Subtitle1'
                        halign: 'center'
                        height: self.texture_size[1]
                    MDLabel:
                        id: home_email
                        text: 'email'
                        font_style: 'Caption'
                        halign: 'center'
                        height: self.texture_size[1]
                    MDSeparator:
                        height: '4dp'
                
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Deposit'
                        on_press:
                            root.manager.current = 'deposit'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'bank-transfer-in'
                    OneLineIconListItem:
                        text: 'Transfer'
                        on_press:
                            root.manager.current = 'transfer'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'transfer'
                    OneLineIconListItem:
                        text: 'Virtual Card'
                        on_press:
                            root.manager.current = 'vir_card'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'credit-card'
                    MDSeparator:
                        height: '4dp'
                    OneLineIconListItem:
                        text: 'Map'
                        on_press:
                            root.manager.current = 'map'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'map'
                    OneLineIconListItem:
                        text: 'Interest Calculator'
                        on_press:
                            root.manager.current = 'interest'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'calculator-variant'
                    MDSeparator:
                        height: '4dp'
                    OneLineIconListItem:
                        text: 'Settings'
                        on_press: 
                            root.manager.current = 'set'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'nut'
                    OneLineIconListItem:
                        text: 'Logout'
                        on_press: 
                            root.manager.current = 'login'
                            nav_drawer.set_state('toggle')
                        IconLeftWidget:
                            icon: 'logout'
                    OneLineIconListItem:
                        text: 'Exit'
                        on_press: 
                            quit()
                        IconLeftWidget:
                            icon: 'exit-to-app'


<MapScreen>:
    name: 'map'
    MapView:
        lat: 26.2235
        lon: 50.5876
        zoom: 12

    MDFloatingActionButton:
        icon: 'home'
        pos_hint: {'center_x':0.9, 'center_y':0.1}
        on_press: root.manager.current = 'home'


<CardScreen>:
    name: 'vir_card'
    MDToolbar:
        pos_hint: {"top":1}
        title: "Virtual Card"
        elevation: 20
        left_action_items: [['arrow-left', lambda x: root.back()]]
    MDCard:
        orientation: 'vertical'
        md_bg_color: (0, 9/255, 31/255, 1)
        size_hint: None, None
        size: root.width - (dp(30)), "200dp"
        elevation: 20
        radius: '10dp'
        pos_hint: {"center_x": .5, "center_y": 0.7}

        BoxLayout:
            orientation: 'horizontal'
            MDCard:
                size_hint: None, None
                size: root.width - 180, '30dp'
                pos_hint: {'center_y':0.1}
                md_bg_color: (240/255, 240/255, 240/255, 1)
            MDCard: 
                size_hint: None, None
                size: '30dp', '30dp'
                pos_hint: {'center_x':0.5 ,'center_y':0.1}
                md_bg_color: (35/255, 123/255, 0, 1)
                Image:
                    source: 'wifi.png'
        BoxLayout:
            padding: '10dp'
            orientation: 'vertical'
            MDLabel:
                id: card_number
                text: '1234  5678  9012  3456'
                font_style: 'Button'
                font_size: '23dp'
                theme_text_color: "Custom"
                text_color: 240/255, 240/255, 240/255, 1
                pos_hint: {'center_y':0.8}
        BoxLayout:
            orientation: 'horizontal'
            padding: '15dp'
            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    id: card_f_name
                    text: 'Username'
                    font_style: 'Button'
                    font_size: '10dp'
                    theme_text_color: "Custom"
                    text_color: 240/255, 240/255, 240/255, 1
                MDLabel:
                    id: card_l_name
                    text: 'Username'
                    font_style: 'Button'
                    font_size: '10dp'
                    theme_text_color: "Custom"
                    text_color: 240/255, 240/255, 240/255, 1
            MDLabel:
                text: '07/25'
                font_style: 'Button'
                font_size: '10dp'
                theme_text_color: "Custom"
                text_color: 240/255, 240/255, 240/255, 1
            Image:
                source: 'mastercard.png'
                size_hint: None, None
                size: '60dp', '60dp'
                pos_hint: {'center_y':0.5}


<DepositScreen>:
    name: 'deposit'
    MDCard:
        orientation: "vertical"
        size_hint: None, None
        size: 300, 400
        radius: '10dp'
        elevation: 10
        padding: 25
        spacing: 25
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: 'Deposit Money'
            halign: 'center'
            pos_hint: {'center_y':0.95}
            font_style: 'Button'
            font_size: '32dp'

        BoxLayout:
            orientation: 'horizontal'
            width: 300
            spacing: 50
            MDTextField:
                id: name_first
                hint_text : "First Name"
                mode: "rectangle"
                size_hint_x : None
                width : 100
            MDTextField:
                id: name_last
                hint_text : "Last Name"
                mode: "rectangle"
                size_hint_x : None
                width : 100

        BoxLayout:
            orientation: 'horizontal'
            width: 300
            spacing: 50
            MDTextField:
                id: card_num
                hint_text : "Card Number"
                input_filter: 'int'
                max_text_length: 16
                mode: "rectangle"
                size_hint_x : None
                width : 150
            MDTextField:
                id: cvc_num
                hint_text : "CVC"
                input_filter: 'int'
                max_text_length: 3
                mode: "rectangle"
                icon_right_color : app.theme_cls.primary_color
                size_hint_x : None
                width : 50

        MDTextField:
            id: deposit_amount
            hint_text : "Amount"
            helper_text : "Enter amount to be deposited"
            helper_text_mode : "on_focus"
            input_filter: 'int'
            mode: "rectangle"
            icon_right : "bitcoin"
            icon_right_color : app.theme_cls.primary_color
            pos_hint : {'center_x':0.5, 'center_y':0.4}
            size_hint_x : None
            width : 250

        BoxLayout:
            orientation: 'horizontal'
            spacing: 25
            pos_hint: {'center_x':0.75}
            MDFlatButton:
                text: 'Back'
                on_press: root.manager.current = 'home'
            MDRaisedButton:
                text: 'DEPOSIT'
                on_press:
                    root.dep_btn()
                    # root.update_dep()

<InterestScreen>:
    name: 'interest'
    MDCard:
        orientation: "vertical"
        size_hint: None, None
        size: 300, 450
        radius: '10dp'
        elevation: 10
        padding: 25
        spacing: 25
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: 'S.I and C.I'
            halign: 'center'
            pos_hint: {'center_y':0.95}
            font_style: 'Button'
            font_size: '32dp'

        Widget:
            size_hint_y: None
            height: 160

        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            MDTextField:
                id: prin_am
                input_filter: 'int'
                hint_text : "Principal Amount"
                mode: "rectangle"
                size_hint_x : None
                width : 250
                required: True
            MDTextField:
                id: rate
                input_filter: 'int'
                hint_text : "Rate"
                mode: "rectangle"
                size_hint_x : None
                width : 250
                required: True
            MDTextField:
                id: time_i
                input_filter: 'int'
                hint_text : "Time(years)"
                helper_text_mode: 'on_focus'
                mode: "rectangle"
                size_hint_x : None
                width : 250
                required: True
            MDTextField:
                id: n_ci
                input_filter: 'int'
                hint_text : "Compound Period"
                helper_text: 'Number of times to be compounder'
                helper_text_mode: 'on_focus'
                mode: "rectangle"
                size_hint_x : None
                width : 250
                required: True

        BoxLayout:
            orientation: 'horizontal'
            spacing: 25
            pos_hint: {'center_x':0.68}
            MDFlatButton:
                text: 'Back'
                on_press: root.manager.current = 'home'
            MDRaisedButton:
                text: 'CALCULATE'
                on_press: root.calculate_btn()


<TransferScreen>:
    name: 'transfer'
    MDLabel:
        text: 'Transfer Money'
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'Button'
        font_size: '50dp'

    MDTextField:
        id: transfer_acc_mail
        hint_text : "Email"
        helper_text : "Enter receiver's email"
        helper_text_mode : "on_focus"
        mode: "rectangle"
        icon_right : "email"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y':0.65}
        size_hint_x : None
        width : 250

    MDTextField:
        id: amount_transfer
        input_filter: 'int'
        hint_text : "Amount"
        helper_text : "Enter amount to be transfered"
        helper_text_mode : "on_focus"
        mode: "rectangle"
        icon_right : "bitcoin"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y':0.53}
        size_hint_x : None
        width : 250

    MDTextField:
        id: reg_pass
        hint_text : "Password"
        helper_text : "Enter your account password"
        helper_text_mode : "on_focus"
        mode: "rectangle"
        icon_right : "key"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y':0.4}
        size_hint_x : None
        width : 250
    
    MDRectangleFlatButton:
        text: 'Transfer Money'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
        on_press: root.transfer_btn()

    MDFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.17}
        on_press: root.manager.current = 'home'


<SettingScreen>:
    name: 'set'
    MDToolbar:
        id: toolbar
        pos_hint: {"top":1}
        title: "Settings"
        elevation: 20
        left_action_items: [['arrow-left', lambda x: root.home()]]
    ScrollView:
        pos_hint: {'center_y':0.4}
        MDList:
            MDSeparator:
                height: '20dp'
                MDLabel:
                    text: 'App settings'
                    font_style: 'Button'
                    halign: 'left'
            OneLineIconListItem:
                text: 'Mode'
                on_press: app.theme_ch()
                IconLeftWidget:
                    icon: 'theme-light-dark'
            OneLineIconListItem:
                text: 'Theme'
                on_press: app.show_theme_picker()
                IconLeftWidget:
                    icon: 'eyedropper'
            MDSeparator:
                height: '20dp'
                MDLabel:
                    text: 'General settings'
                    font_style: 'Button'
                    halign: 'left'
            OneLineIconListItem:
                text: 'Support'
                on_press: app.support_open()
                IconLeftWidget:
                    icon: 'link'
"""

class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    def login_info(self):
        self.url = "https://myapp-data-f2c21-default-rtdb.firebaseio.com/.json"
        log_email = self.ids.log_email.text
        log_pass = self.ids.log_pass.text
        self.helper = Builder.load_string(username_helper)
        supported_email = log_email.replace('.','-')
        supported_pass = log_pass.replace('.','-')
        request = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails = set()
        for key,value in data.items():
            emails.add(key)
        if supported_email in emails and supported_pass == data[supported_email]['Password']:
            self.username = data[supported_email]['Username']
            self.name_first = data[supported_email]['Name_First']
            self.name_last = data[supported_email]['Name_Last']
            self.password = data[supported_email]['Password']
            self.your_balance = data[supported_email]['Balance']
            self.card_num_disp = data[supported_email]['Card_Number']
            self.login_check = True
            self.parent.current = 'home'
            self.manager.get_screen('home').ids.display_amount.text = f'₹ {self.your_balance}'
            self.manager.get_screen('home').ids.home_username.text = f'{self.username}'
            self.manager.get_screen('home').ids.home_email.text = f'{log_email}'
            self.manager.get_screen('vir_card').ids.card_f_name.text = f'{self.name_first}'
            self.manager.get_screen('vir_card').ids.card_l_name.text = f'{self.name_last}'
            self.manager.get_screen('vir_card').ids.card_number.text = f'{self.card_num_disp}'
            self.ids.log_email.text = ''
            self.ids.log_pass.text = ''
            print(self.username)
        else:
            self.user_dialog = MDDialog(
                    title='Error!',
                    text='Please enter correct password or email.',
                    buttons=[
                            MDRaisedButton(text="CLOSE", on_release=self.close_dial),
                            ])
            self.user_dialog.open()
    auth = 'i7pVzE2g7Ep6sWsHkaNPSowfyfIs7peOPFG86EEA'
    
    def close_dial(self, obj):
        self.user_dialog.dismiss()


class RegisterScreen(Screen):
    def register_info(self):
        self.url = "https://myapp-data-f2c21-default-rtdb.firebaseio.com/.json"
        reg_name_first = self.ids.reg_name_first.text
        reg_name_last = self.ids.reg_name_last.text
        reg_name_user = self.ids.reg_name_user.text
        reg_email = self.ids.reg_email.text
        reg_pass = self.ids.reg_pass.text
        balance = self.manager.get_screen('home').ids.display_amount.text
        #card
        b = 10**(4-1)
        c = (10**4)-1
        num_card_1 = random.randint(b, c)
        num_card_2 = random.randint(b, c)
        num_card_3 = random.randint(b, c)
        num_card_4 = random.randint(b, c)
        num_card = str(num_card_1)+" "+str(num_card_2)+" "+str(num_card_3)+" "+str(num_card_4)
        self.manager.get_screen('vir_card').ids.card_number.text = f'{num_card}'
        #card-end
        register_info = str({f'\"{reg_email}\":{{"Name_First":\"{reg_name_first}\","Name_Last":\"{reg_name_last}\","Username":\"{reg_name_user}\","Password":\"{reg_pass}\","Balance":\"{balance}\","Card_Number":\"{num_card}\"}}'})
        register_info = register_info.replace(".","-")
        register_info = register_info.replace("\'","")
        to_database = json.loads(register_info)
        print((to_database))
        requests.patch(url = self.url, json = to_database)
        self.parent.current = 'login'
        Snackbar(
            text="Account Created. Please Login.",
            duration="2",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()

    def close_user_dialog(self, obj):
        self.user_dialog.dismiss()


class HomeScreen(Screen):
    pass


class MapScreen(Screen):
    pass


class CardScreen(Screen):
    def back(self):
        self.parent.current = 'home'


class DepositScreen(Screen):
    def dep_btn(self):
        dep_f_name =  self.ids.name_first.text
        dep_l_name =  self.ids.name_last.text
        dep_card = self.ids.card_num.text
        dep_cvc = self.ids.cvc_num.text
        dep_am = self.ids.deposit_amount.text
        if dep_f_name == '' or dep_l_name == '':
            Snackbar(
            text="Please Enter Full Name",
            duration="1",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif dep_card == '':
            Snackbar(
            text="Please Enter Card Number",
            duration="1",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif dep_cvc == '':
            Snackbar(
            text="Please Enter CVC Number",
            duration="1",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif dep_am == '':
            Snackbar(
            text="Please Enter Amount to be deposited",
            duration="1",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        else:
            self.deposit_dialog = MDDialog(
                    title='Confirmation',
                    text=f'Are you sure you want to deposit ₹ {dep_am}',
                    buttons=[
                            MDFlatButton(text="CANCEL", on_release=self.close_dialog_dep),
                            MDRaisedButton(text="YES", on_release=self.dep_done),
                            ])
            self.deposit_dialog.open()

    def close_dialog_dep(self, obj):
        self.deposit_dialog.dismiss()

    def dep_done(self, obj):
        dep_am = self.ids.deposit_amount.text
        dis_am = self.manager.get_screen('home').ids.display_amount.text
        dis_am_am = dis_am.replace("₹","")
        post_dep = int(dis_am_am) + int(dep_am)
        self.manager.get_screen('home').ids.display_amount.text = f'₹ {post_dep}'
        Snackbar(
            text="Successfully deposited",
            bg_color=(1, 1, 1, 1),
            duration="1",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        self.ids.deposit_amount.text = ""
        self.ids.cvc_num.text = ""
        self.ids.card_num.text = ""
        self.ids.name_first.text = ""
        self.ids.name_last.text = ""
        self.parent.current = 'home'
        self.deposit_dialog.dismiss()
    
    # def update_dep(self):


class InterestScreen(Screen):
    def calculate_btn(self):
        prin = self.ids.prin_am.text
        rate = self.ids.rate.text
        time = self.ids.time_i.text
        n = self.ids.n_ci.text
        power = int(n) * int(time)
        r_by_n = int(rate)/int(n)
        pi = (int(prin) * int(rate) * int(time))/100
        ci = int(prin) * (1 + r_by_n)**int(power)
        self.interest_dialog = MDDialog(
                        text=f'Principal interst = ₹ {round(pi,2)}\n\nCompound interst = ₹ {round(ci,2)}',
                        buttons=[
                        MDFlatButton(text="CANCEL", on_release=self.close_dialog_i),
                        MDRaisedButton(text="HOME", on_release=self.home_i),
                        ])
        self.interest_dialog.open()
    
    def close_dialog_i(self, obj):
        self.interest_dialog.dismiss()
        self.ids.prin_am.text = ""
        self.ids.rate.text = ""
        self.ids.time_i.text = ""
        self.ids.n_ci.text = ""
    
    def home_i(self, obj):
        self.interest_dialog.dismiss()
        self.parent.current = 'home'
        self.ids.prin_am.text = ""
        self.ids.rate.text = ""
        self.ids.time_i.text = ""
        self.ids.n_ci.text = ""


class TransferScreen(Screen):
    def transfer_btn(self):
        tr_pass = self.ids.reg_pass.text
        tr_email = self.ids.transfer_acc_mail.text
        tr_amount = self.ids.amount_transfer.text
        rec_acc = self.ids.transfer_acc_mail.text
        if tr_pass == '' and tr_email == '' and tr_amount == '':
            Snackbar(
            text="Please fill all the details",
            duration="2",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif tr_email == '':
            Snackbar(
            text="Please Enter Receiver's Email",
            duration="2",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif tr_amount == '':
            Snackbar(
            text="Please Enter Amount",
            duration="2",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        elif tr_pass == '':
            Snackbar(
            text="Please Enter Password",
            duration="2",
            snackbar_animation_dir="Bottom",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7
        ).open()
        else:
            self.transfer_dialog = MDDialog(
                title='Confirmation',
                text=f'Are you sure you want to trasnfer ₹ {tr_amount} to {rec_acc}',
                buttons=[
                        MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                        MDRaisedButton(text="YES", on_release=self.tran_done),
                        ])
            self.transfer_dialog.open()

    def close_dialog(self, obj):
        self.transfer_dialog.dismiss()
    
    def close_dialog_in(self, obj):
        self.insuff_dialog.dismiss()
        self.transfer_dialog.dismiss()
        self.manager.get_screen('transfer').ids.amount_transfer.text = ""
        self.manager.get_screen('transfer').ids.transfer_acc_mail.text = ""
        self.manager.get_screen('transfer').ids.reg_pass.text = ""

    def dep_screen(self, obj):
        self.parent.current = 'deposit'
        self.insuff_dialog.dismiss()
        self.transfer_dialog.dismiss()

    def tran_done(self, obj):
        
        tr_am = self.ids.amount_transfer.text
        dis_am = self.manager.get_screen('home').ids.display_amount.text
        dis_am_am = dis_am.replace("₹","")
        if int(tr_am) > int(dis_am_am):
            self.insuff_dialog = MDDialog(
                    title='Insufficient Balance',
                    text='Transfer amount is greater than your current balance.',
                    buttons=[
                            MDFlatButton(text="CLOSE", on_release=self.close_dialog_in),
                            MDRaisedButton(text="DEPOSIT", on_release=self.dep_screen),
                            ])
            self.insuff_dialog.open()
        else:
            post_tran = int(dis_am_am) - int(tr_am)
            self.manager.get_screen('home').ids.display_amount.text = f'₹ {post_tran}'
            Snackbar(
                text="Successfully transfered",
                bg_color=(1, 1, 1, 1),
                duration="1",
                snackbar_animation_dir="Bottom",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.7
            ).open()
            self.ids.reg_pass.text = ""
            self.ids.transfer_acc_mail.text = ""
            self.ids.amount_transfer.text = ""
            self.parent.current = 'home'
            self.transfer_dialog.dismiss()


class SettingScreen(Screen):
    def home(self):
        self.parent.current = 'home'


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(MapScreen(name='map'))
sm.add_widget(DepositScreen(name='deposit'))
sm.add_widget(InterestScreen(name='interest'))
sm.add_widget(TransferScreen(name='transfer'))
sm.add_widget(CardScreen(name='vir_card'))
sm.add_widget(SettingScreen(name='set'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.helper = Builder.load_string(username_helper)
        self.url = "https://myapp-data-f2c21-default-rtdb.firebaseio.com/"
        return self.helper

    def theme_ch(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = "Yellow"
        else:
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = "DeepOrange"

    def support_open(self):
        webbrowser.open_new("https://safe-bank.netlify.app")

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    
myapp = DemoApp
DemoApp().run()
