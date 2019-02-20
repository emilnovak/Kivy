import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatLayoutApp()
flApp.run()
