from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty
from socket import *

class AgHaritalama(Screen):
    def portTarama(self,ip_adres):
        print ("Port Tarama Basladi %s".format(ip_adres))
        hedefIP = ip_adres
        ports = [22, 23, 25, 53, 80, 443, 3389] #yaygin portlar ftp, telnet, smtp, dns, http, https, rdp
        for i in ports:
            s = socket(AF_INET, SOCK_STREAM)
            sonuc = s.connect_ex((hedefIP, i))
            if(sonuc == 0) :
                print ('Port %d: ACIK') % (i,)
                s.close()

class AgHaritalamaApp(App):
    ip = StringProperty(None)
    def build(self):
        return AgHaritalama()

if __name__ == "__main__":
    AgHaritalamaApp().run()