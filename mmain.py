from random import random as rm
from random import choice as ch
from threading import Thread as th
from time import sleep as sl
from random import shuffle as sf


class vr:
    def __init__(self):
        self.veri_kayıt_uzunluğu=8
        self.olacaklar=[]# sıra 0,1,2,3,4,...
        self.olarka=[]
        self.ay=","
        self.olumluluk=[]
        self.scn=[-2,-1,0,1,2]
        self.maks=len(self.scn)-1
        self.maksdepolama=len(self.scn)**self.veri_kayıt_uzunluğu
        for i in range(self.veri_kayıt_uzunluğu):
            self.olacaklar.append(self.scn[0])
        d=1
        if d==1:None
        else:
            for i in range(self.veri_kayıt_uzunluğu):
                self.olarka.append(0)
            with open("eşitlenebilir.txt", "w+") as d:
                d.writelines("")
            with open("eşitlenebilir.txt", "a+") as d:
                for i in range(len(self.scn)**self.veri_kayıt_uzunluğu):
                    print(i+1)
                    if 1:
                        self.olumluluk=[]
                        self.olarka=[]
                        bt=0
                        tx=""
                        sr=0
                        for iii in range(len(self.olacaklar)):
                            if self.veri_kayıt_uzunluğu-1==iii:
                                tx=tx+str(self.olacaklar[iii])
                            else:
                                tx="{};{}".format(str(self.olacaklar[iii]),tx)
                        a=0
                        for iii in self.olacaklar:
                            if iii!=self.scn[-1]:
                                a=1
                        if a==1:
                            tx="{},".format(tx)
                        d.writelines(tx)
                        for iii in range(len(self.olacaklar)):
                            if self.olacaklar[iii]==self.scn[-1]:
                                self.olumluluk.append(1)
                            else:
                                self.olumluluk.append(0)
                        if i==len(self.scn)**self.veri_kayıt_uzunluğu-1:None
                        elif self.olumluluk[0]==1:
                            for iii in range(len(self.olumluluk)):
                                if self.olumluluk[iii]==1 and bt==0:
                                    sr=sr+1
                                else:
                                    bt=1
                            for iii in range(sr):
                                self.olacaklar[iii]=self.scn[0]
                            self.olacaklar[iii+1]=self.scn[self.scn.index(self.olacaklar[iii+1])+1]
                        else:
                            self.olacaklar[0]=self.scn[self.scn.index(self.olacaklar[0])+1]
class al_dönüştür:
    def __init__(self):
        self.giriş=""
    def girdi(self):
        with open("girdi.txt", "r+") as d:
            self.giriş=d.readlines()[0]
    def girdi(self):
        with open("girdi.txt", "r+") as d:
            self.giriş=d.readlines()[0]
    def dönüştür(self):
        a=1
        kayıt=[]
        with open("adım1.txt", "w+") as d:
            d.write("")
        for i in range(len(self.giriş)):
            if i==len(self.giriş)-1:
                while a==1:
                    text=str(id(self.giriş[i])**1.33333333333*rm())[:-4]
                    if not text in kayıt:
                        a=0
            else:
                while a==1:
                    text=str(id(self.giriş[i])**1.33333333333*rm())[:-4]+","
                    if not text in kayıt:
                        a=0
            kayıt.append(text)
            a=1
            with open("adım1.txt", "a+") as dosya:
                dosya.writelines(text)
class ord_eşitliği:
    def __init__(self):
        self.veri1=""
        self.veri2=""
    def veri_eşitle(self):
        dv=0
        stp=0
        with open("oes.txt", "w+")as d:
            d.writelines("")
        with open("girdi.txt", "r+")as d:
            u=len(d.readlines()[0])
        for i in range(u):
            with open("girdi.txt", "r+")as d:
                self.veri1=d.readlines()[0][i]
            with open("adım1.txt", "r+")as d:
                self.veri2=d.readlines()[0].split(",")[i]
            with open("oes.txt", "r+")as d:
                if i==0:
                    stp=0
                elif i==1:
                    if "{},{};".format(self.veri1,self.veri2) == d.readlines()[0]:
                        stp=1
                    else:
                        stp=0
                elif i>2:
                    kn=d.readlines()[0].split(",")
                    vr="{};{}".format(self.veri1,self.veri2)
                    if vr in kn:
                        stp=1
                    else:
                        stp=0
            with open("oes.txt", "a+")as d:
                if stp==0:
                    if i!=u-1:
                        d.writelines("{};{},".format(self.veri1,self.veri2))
                    else:
                        d.writelines("{};{}".format(self.veri1,self.veri2))
class key_seç:
    def __init__(self):
        self.key1=[]
        self.key2=[]
        self.oes=[]
        self.kull=[]
        with open("key2.txt", "w+")as d:
            d.writelines("")
        with open("key1.txt", "w+")as d:
            d.writelines("")
        with open("oes.txt", "r+")as d:
            for i in d.readlines()[0].split(","):
                self.oes.append(i.split(";"))
        with open("eşitlenebilir.txt", "r+")as d:
            for i in d.readlines()[0].split(","):
                self.kull.append([i.split(";")])
    def keysec(self):
        tx=""
        for i in range(len(self.oes)):
            sc=ch(self.kull)
            self.key1.append([self.oes[i][1],sc[0]])
            self.key2.append(self.oes[i])
            self.kull.remove(sc)
        for i in range(len(self.key1)):
            tt=""
            for ii in range(len(self.key1[i][1])):
                if ii!=len(self.key1[i][1])-1:
                    tt=tt+"{};".format(self.key1[i][1][ii])
                else:
                    tt=tt+"{}".format(self.key1[i][1][ii])
            self.key1[i][1]=tt
        sf(self.key1)
        with open("key1.txt", "a+")as d:
            for i in range(len(self.key1)):
                if i!=len(self.key1):
                    tx=tx+"{}:{},".format(str(self.key1[i][0]),str(self.key1[i][1]))
                else:
                    tx=tx+"{}:{}".format(str(self.key1[i][0]),str(self.key1[i][1]))
            d.writelines(tx)
        tx=""
        sf(self.key2)
        with open("key2.txt", "a+")as d:
            for i in range(len(self.key2)):
                if i != len(self.key2):
                    tx = tx + "{}:{},".format(str(self.key2[i][0]), str(self.key2[i][1]))
                else:
                    tx = tx + "{}:{}".format(str(self.key2[i][0]), str(self.key2[i][1]))
            d.writelines(tx)
class şifreleme:
    def __init__(self):
        self.key1_açık=[]
        self.döndürülmüş=[]
        with open("adım1.txt", "r+")as d:
            self.adım1=d.readlines()[0].split(",")
        with open("key1.txt", "r+")as d:
            self.key1=d.readlines()[0].split(",")
        for i in range(len(self.key1)):
            self.key1_açık.append(self.key1[i].split(":"))
        self.key1_açık.remove([""])
    def döndürme(self):
        for i in range(len(self.adım1)):
            for ii in range(len(self.key1_açık)):
                if self.adım1[i]==self.key1_açık[ii][0]:
                    self.döndürülmüş.append(self.key1_açık[ii][1])
        tx=""
        for i in range(len(self.döndürülmüş)):
            if i!=len(self.döndürülmüş)-1:
                tx=tx+"{},".format(self.döndürülmüş[i])
            else:
                tx=tx+"{}".format(self.döndürülmüş[i])
        with open("mesaj.txt", "w+")as d:
            d.writelines(tx)
vr=vr()
a=al_dönüştür()
ode=ord_eşitliği()
a.girdi()
a.dönüştür()
ode.veri_eşitle()
keo=key_seç()
keo.keysec()
sif=şifreleme()
sif.döndürme()

"""
açıklama filan yok kanka üşendim ama eğer türk isen eğer bazı yakın değişkenleri anlarsın anlamadıklarına birşey yapamam üzgünüm

biraz genel bir açıklama yapayım bari 
bu yazılımda bize verilen girdi.txt dosyası içindeki verileri 2 katmanlı şifreliyoruz 
ilk katman key2.txt dosyası bu dosya rastkeliği kullanıpta kelime değerlerine eşitliyoruz bunun sayesinde tahminsel çözümler olmuyor
ikinci katman ise key1.txt dosyası evet numaraları farklı :) ikinci katman garanti ve çalmaya çalışan kişiye kapak atmak için var 
ve ikinci katmanın algoritlama şeklini istersen değiştirebilirsin ama sana düzenlenebilir şekilde sunduğu için çzülebilme ihtimali var ama bunu çözmek için
karşı tarafın iyi ve hızlı bir algoritmaya ihtiyacı var ama zaten bunu çözse bile ratkele keyimiz olan key2.txt hayatımızı kurtarıyor çünkü bu sadece rastkelelikle alakası yok
bir değere farklı değerleri eşitleyebiliyorsunuz aha karşı taraf şuan içinden ananı sikimm diyor al sana güvenlik key1.txt sızdorsan bile güvendesin ama sen yinede dikkatli ol 
key1.txt ile key2.txt ye iyi bak keylerini etrafa saçma yoksa mutsuz son ile karşılabilirsin haa bu arada bu önemli!!!!!!!!!!
!!!!!!!!!!!!iyi dinle bu uygulamayı kullandıktan sonra girdi.txt , adım1.txt , oes.txt , eşitlenebilir.txt eğer daha kullanmayacaksan mmain.py ı silsen iyi olur çünkü bazıların içerisindeki veriler direk senin keylerini içeriyor
haberin olsunda başıma kalma :)))

haaa birde vr class ının içinde d=1 var eğer eşitlenebilir.txt in yoksa onu 0 yap ama varsa onu 1 yap onu bir kere 0 yapınca ve çalıştırınca 1 yap

birdeee keyleri ve mesaj oluştuktan sonra girdi.txt ve diğer dosyaları silmeyi unutma
"""