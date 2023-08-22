

class keylrçöz:
    def __init__(self):
        self.key1=[]
        self.key2=[]
        self.mesaj=[]
        mes1d=[]
        with open("key2.txt", "r+")as d:
            self.ky2b=d.readlines()[0].split(",")
            for i in self.ky2b:
                self.key2.append(i.split(":"))
        self.key2.remove([""])
        with open("key1.txt", "r+")as d:
            self.key1b=d.readlines()[0].split(",")
            for i in self.key1b:
                self.key1.append(i.split(":"))
        self.key1.remove([""])
        with open("mesaj.txt", "r+")as d:
            self.mesajd=d.readlines()[0].split(",")
        for i in range(len(self.mesajd)):
            self.mesaj.append(self.mesajd[i].split(";"))
        for i in range(len(self.mesaj)):
            mes1d.append([])
            tx=""
            for ii in range(len(self.mesaj[i])):
                tx="{};{}".format(self.mesaj[i][ii],tx)
            mes1d[i].append(tx)
        for i in range(len(mes1d)):
            mes1d[i]=mes1d[i][0]
        termesd=[]
        terind=[]
        terbin=[]
        for i in range(len(mes1d)):
            terind.append(mes1d[i].split(";"))
        for i in range(len(terind)):
            terind[i].reverse()
        for i in range(len(terind)):
            tx=""
            for ii in range(len(terind[i])):
                if ii==0:
                    tx="{}".format(terind[i][0])
                else :
                    tx="{};{}".format(tx,terind[i][ii])
            tt=tx[1:]
            termesd.append(tt)
        self.mesaj=termesd
    def mesajkey1(self):
        mesajc1=[]
        a=0
        for i in range(len(self.mesaj)):
            for ii in range(len(self.key1)):
                if self.key1[ii][1]==self.mesaj[i]:
                    mesajc1.append(self.key1[ii][0])
        self.mesaj=mesajc1
    def mesajkey2(self):
        mesajc2=[]
        for i in range(len(self.mesaj)):
            for ii in range(len(self.key2)):
                if self.mesaj[i]==self.key2[ii][1]:
                    mesajc2.append(self.key2[ii][0])
        self.mesaj=mesajc2
    def metinol(self):
        self.çıktı=""
        for i in self.mesaj:
            self.çıktı="{}{}".format(self.çıktı,i)
    def çıkt(self):
        print(self.çıktı)
        #oh bee zaman bulamadığımdan proje yavaş ilerliyordu bitirdim artık :)
klr=keylrçöz()
klr.mesajkey1()
klr.mesajkey2()
klr.metinol()
klr.çıkt()
print("\n")
input("çıkmak için enter a bas")