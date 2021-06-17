from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
from kivy.uix.image import Image
import json,glob #glob is used to get names of files present in a folder
from datetime import datetime
from pathlib import Path
import random
#from kivy.core.window import Window   use this to set screen color. in line 120

from email.mime.text import MIMEText
import smtplib   #importing server for gmail


Builder.load_file('design.kv')

class HomeScreen(Screen):
    def printinfo(self):
        self.ids.message.text= "This is an email bomber app. here you can bomb your friends email id.Just provide your friends email id and rest leave everything on us"
   
    def goto(self):
        self.manager.current= "Login_screen"


class LoginScreen(Screen):
    def signup(self):
        self.manager.current= "Signup_screen"

    def login(self,uname,pword): #checking if username and password is correct and then opening next page
        with open("users.json") as myfile:
            users=json.load(myfile) #this opens json file in the correct form of dictionary
        
        if uname in users and users[uname]['password']==pword:
            self.manager.current= "Login_success_screen"
        else:
            self.ids.message.text="Wrong username or password"

    def forgotpassword(self):
        self.manager.current= "Forgot_password_screen"



class LoginsuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction= 'right'
        self.manager.current= "Login_screen"
        
    def send_email(self,address):   #note fn name and file name are same (no problem in this)
        from_email="q084zainab@gmail.com"
        from_password="1234zainab"
        to_email=address

        subject="MAIL BOMBER"
        message="hii there, hope you are doing good.\n We are just testing our <strong>Email Bomber Application</strong>" 

        msg=MIMEText(message, 'html')  #telling gmail that our message is a type of html text
        msg["Subject"]=subject
        msg['To']=to_email
        msg['From']=from_email

        gmail=smtplib.SMTP('smtp.gmail.com',587)   #server for gamil
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)  #loginng in gmail
        gmail.send_message(msg) #sending meassage    

        self.ids.output.text="Now ask the receiver to check his email."   
            

class SignupScreen(Screen): #here we will store all sign up data in a json file
    def add_entry(self,uname,pword):
        with open("users.json") as myfile:
            users=json.load(myfile)  #it will result in a dictionary

            users[uname]={'username':uname, 'password':pword,
            'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json",'w') as myfile:
            json.dump(users,myfile)

        self.manager.current= "Signup_success_screen"
    
    def goto(self):
        self.manager.transition.direction='right'
        self.manager.current="Login_screen"




class SignupsuccessScreen(Screen):
    def goto(self):
        self.manager.transition.direction= 'right'
        self.manager.current= "Login_screen"  

class ForgotPasswordScreen(Screen):
    def getpassword(self,uname):
        with open("users.json") as myfile:
            users=json.load(myfile)
        if uname in users:
            self.ids.pwd.text= "Your Password is" +" "+ users[uname]['password']
        else:
            self.ids.pwd.text= "Username Not Found"
    
    def goto(self):
        self.manager.transition.direction='right'
        self.manager.current="Login_screen"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        #Window.clearcolor= (48,0,0,1)  making all screen red
        return RootWidget()







if __name__=="__main__":
    MainApp().run()