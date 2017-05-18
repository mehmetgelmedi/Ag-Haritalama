from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty


class AgHaritalama(Screen):
    def portTarama(self,ip_adres):
        print("ip adresi : %s" %ip_adres)
    pass

class AgHaritalamaApp(App):
    ip = StringProperty(None)
    def build(self):
        return AgHaritalama()
        

if __name__ == "__main__":
    AgHaritalamaApp().run()
