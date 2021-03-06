from socket import *
from tkinter import *
import tkinter.messagebox as tm
from threading import Thread
import subprocess

class AgHaritalama():
    def portTarama(ip_adres):
        print ("Port Tarama Basladi {0}".format(ip_adres))
        hedefIP = ip_adres
        portlar = [22, 23, 25, 53, 80, 443, 3389] #yaygin portlar ftp, telnet, smtp, dns, http, https, rdp
        thread_listesi = []
        for i in portlar:
            t = Thread(target=AgHaritalama.portTaramaThread, args=(hedefIP,i,))
            t.daemon = True
            thread_listesi.append(t)

        for t in thread_listesi:
            t.start()

    def portTaramaThread(hedefIP,port):
        s = socket(AF_INET, SOCK_STREAM)
        sonuc = s.connect_ex((hedefIP, port))
        print ('%d Port taraniyor..' % port)
        if(sonuc == 0) :
            print ('Port %d: ACIK' % port)
            tm.showinfo("Port Tarama Sonuclari", "Port %d: ACIK\n" % port)
            s.close()
        else:
            print ('Port %d: KAPALI' % port)
            s.close()

    def pingAraci(ip):
        try:
            sonuc = subprocess.check_output("ping " + ip)
            if sonuc != 0:
                tm.showinfo("Ping Sonuclari",sonuc.decode('unicode_escape').encode('utf-8'))
        except:
            tm.showinfo("Ping Sonuclari","IP Bulunamadi !")

    def arpTara(gateway):
        try:
            #10.39.168.1
            print (""+gateway) 
            sonuc = subprocess.check_output("python2 arpmac.py " + gateway)
            sonuc = sonuc.decode('unicode_escape').encode('utf-8')
            tm.showinfo("Ag Haritalama",sonuc)
        except:
            tm.showinfo("Ag Haritalama","Bir hata olustu!")
        #tm.showinfo("Mac / Arp Sonuclari",bilgi)


class AgHaritalamaFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_IPAdres = Label(self, text="IP Adres :")

        self.entry_IPAdres = Entry(self)

        self.lbl_IPAdres.grid(row=0, sticky=NW)
        self.entry_IPAdres.grid(row=0, column=1)

        self.btn_PortTara = Button(self, text="Port Tara", command = self.btn_PortTara_Tik)
        self.btn_PortTara.grid(columnspan=2)

        self.lbl_ArpTara = Label(self, text="Ag Gecidi :")
        self.lbl_ArpTara.grid(row=2, sticky=NW)

        self.entry_Gateway = Entry(self)
        self.entry_Gateway.grid(row=2, column=1)

        self.btn_ArpTara = Button(self, text="Mac / Arp Tara", command = self.btn_ArpTara_Tik)
        self.btn_ArpTara.grid(columnspan=2)


        self.lbl_PingAraci = Label(self, text="IP veya Hostname :")
        self.lbl_PingAraci.grid(row=4, sticky=NW)

        self.entry_IPveyaHost = Entry(self)
        self.entry_IPveyaHost.grid(row=4, column=1)

        self.btn_PingAraci = Button(self, text="Ping", command = self.btn_PingAraci_Tik)
        self.btn_PingAraci.grid(columnspan=4)

        self.pack()

    def btn_PortTara_Tik(self):
        ipadres=self.entry_IPAdres.get()
        t=Thread(target=AgHaritalama.portTarama, args=(ipadres,))
        t.daemon=True
        t.start()
        #AgHaritalama.portTarama(ipadres)

    def btn_ArpTara_Tik(self):
        varsayilanAgGecidi = self.entry_Gateway.get()
        t=Thread(target=AgHaritalama.arpTara, args=(varsayilanAgGecidi,))
        t.daemon=True
        t.start()

    def btn_PingAraci_Tik(self):
        ipadres=self.entry_IPveyaHost.get()
        t=Thread(target=AgHaritalama.pingAraci, args=(ipadres,))
        t.daemon=True
        t.start()


def main():
    root = Tk()
    root.title("Ag Haritalama")
    root.geometry("300x400")
    root.resizable(0,0)
    ahF = AgHaritalamaFrame(root)
    root.mainloop()
    #AgHaritalama.arpTarama()

if __name__ == '__main__':
    main()
