from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
from kivy.core.window import Window
Window.size=(700,450)
Window.clearcolor=(1,1,1,1)
class numberguess(App):
    def build(self):
        self.t1= TextInput(text="Guess your number in between 1 to 10:")
        b=BoxLayout(orientation="vertical",spacing=10,padding=30)
        b1=Button(text="start",on_press=self.game)
        self.l=Label(text="",color=(0,1,0,1),font_size=(25))
        b.add_widget(self.l)
        b.add_widget(self.t1)
        b.add_widget(b1)
        return b
    def game(self,obj):
        guess = int(self.t1.text)
        num= random.randint(1, 10)
        b=str(num)
        if guess == num:
            self.l.text=("congratulations! you won! \n Computer's Guess: "+b)
        else:
            self.l.text=("Nope...Sorry. try again! \n Computer's Guess: "+b)
b1= numberguess()
b1.run()