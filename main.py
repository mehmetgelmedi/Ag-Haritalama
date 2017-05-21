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

        self.lbl_IPAdres.grid(row=0, sticky=E)
        self.entry_IPAdres.grid(row=0, column=1)

        self.btn_PortTara = Button(self, text="Port Tara", command = self.btn_PortTara_Tik)
        self.btn_PortTara.grid(columnspan=2)

        self.pack()

    def btn_PortTara_Tik(self):
        ipadres=self.entry_IPAdres.get()
        AgHaritalama.portTarama(ipadres)

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