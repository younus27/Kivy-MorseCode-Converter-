import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import morse 
import pyperclip
from kivy.properties import StringProperty
from kivy.core.window import Window
#Window.clearcolor = (.1176, .3451,.4706, 1)
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    textVar = StringProperty()

    def go(self,inputtext):
        try:
            return morse.encrypt(inputtext.text.upper())
        except:
            return "Invalid Entry" 
    def copy1(self,inputtext):
        pyperclip.copy(inputtext)
class ScreenThree(Screen):
    morseVar = StringProperty()
    def go2(self,inputtext):
        try:
            return morse.decrypt(inputtext.text)
        except:
            return "Invalid Entry" 
    def copy2(self,inputtext):
        pyperclip.copy(inputtext)
class ScreenHelp(Screen):
    pass
class ScreenAbout(Screen):
    pass
class ScreenRecent(Screen):
    pass
'''
screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenHelp(name="screen_help"))
screen_manager.add_widget(ScreenAbout(name="screen_about"))
'''





class KivyminiApp(App):


    def build(self):
        return Builder.load_file("kivymini.kv")

sample_app = KivyminiApp()
sample_app.run()
