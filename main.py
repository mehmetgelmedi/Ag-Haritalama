from socket import *
from tkinter import *
import tkinter.messagebox as tm

class AgHaritalama():
    def portTarama(ip_adres):
        print ("Port Tarama Basladi {0}".format(ip_adres))
        hedefIP = ip_adres
        portlar = [22, 23, 25, 53, 80, 443, 3389] #yaygin portlar ftp, telnet, smtp, dns, http, https, rdp
        acikPortlar=''
        for i in portlar:
            s = socket(AF_INET, SOCK_STREAM)
            sonuc = s.connect_ex((hedefIP, i))
            print ('%d Port taraniyor..' % i)
            if(sonuc == 0) :
                print ('Port %d: ACIK' % i)
                acikPortlar+='Port %d: ACIK\n' % i
                s.close()
        tm.showinfo("Port Tarama Sonuclari", acikPortlar)

class AgHaritalamaFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_IPAdres = Label(self, text="IP Adres :")

        self.entry_IPAdres = Entry(self)

        self.lbl_IPAdres.grid(row=0, sticky=NW)
        self.entry_IPAdres.grid(row=0, column=1)

        self.btn_PortTara = Button(self, text="Port Tara", command = self.btn_PortTara_Tik)
        self.btn_PortTara.grid(columnspan=2)

        self.lbl_ArpTara = Label(self, text="Mac / Arp Tarama")
        self.lbl_ArpTara.grid(row=2, sticky=NW)

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
        AgHaritalama.portTarama(ipadres)

    def btn_ArpTara_Tik(self):
        print("Mac / Arp Tarama \n")

    def btn_PingAraci_Tik(self):
        print("Ping Araci \n")


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