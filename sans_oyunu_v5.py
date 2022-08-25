print("\n\n\n")
import os
from re import X
import time
import random
import linecache
import itertools
os.system('cls')

def para(line):
    x=line.split("#")
    d=x[1]
    return int(d)

def sayi(line):
    x=line.split("#")
    d=x[3]
    return int(d)

def miktar(line):
    x=line.split("#")
    d=x[2]
    return float(d)
    
def ad(line):
    x=line.split("#")
    return x[0]

def check(list):
    check=0
    for x in list:
        if x>1000:
            check=1
    return int(check)

def winner(list):
    count=0
    for x in list:
        if x>1000:
            count=count+1
        """ elif x>0 and x<1000:
            count=count+1 """
    return count


handle=open(r"C:\Users\mhdme\OneDrive\Masaüstü\pycodes\odev2.txt","r+")
adlar=list()
paralar=list()
miktarlar=list()
sayilar=list()
satirsayisi=0
for x in handle:
    paralar.append(para(x))
    miktarlar.append(miktar(x))
    sayilar.append(sayi(x))
    adlar.append(ad(x))
    satirsayisi+=1
    #print(x)
print(adlar)
print(paralar)
print(miktarlar)
print(sayilar)
print("lines =",satirsayisi)

sayilar_handle=open(r"C:\Users\mhdme\OneDrive\Masaüstü\pycodes\sayilar.txt","r+")
sayi_sirasi=list()
for x in sayilar_handle:
    x=x.strip()
    sayi_sirasi.append(x)

masaparasi=0
tur=0
p=0
while True: #check(paralar)==1:
    
    print("Tur: ",tur)
    enzenginindex=paralar.index(max(paralar))
    enzenginkisi=adlar[enzenginindex]     #en zengin kişiyi bulmak
    print("en zengin kişi:",enzenginkisi,max(paralar) )

    i=int(sayi_sirasi[p])
    #i=7 # i have to change this 10 to satirsayisi
    sans=i
    temppara=list()
    temppara2=list()
    temppara.clear()   #to delete all temporary list elements
    temppara2.clear()
    print("şanslı sayı=",i)
    #temppara=list()
    arti=1
    if i not in sayilar: # i is the şanslı sayı
        print(paralar)
        print("sorry no one choosed this number")
        arti=0
    else:
        print("i is :",i)
        indexi=sayilar.index(i) # index of lucky number
        print("indexi =",indexi) #i dont have to show the index
        print(adlar[indexi],"choosed that lucky number")
    for i,j in zip(paralar,miktarlar):
        i=i-i*j
        temppara.append(i)
    for i,j in zip(paralar,miktarlar):
        i=i*j
        temppara2.append(i)
    print("this is temp(elindeki para):",temppara)
    print("this is temp2(yatırdığı para):",temppara2)
    masaparasi=masaparasi+sum(temppara2)   # yatırılan parayı masa parasına eklemek
    for w in range(len(paralar)):        #i have to use range because int object is not iterable
        paralar[w]=temppara[w]
        #print(w)
    if arti==1:
        paralar[indexi]=temppara[indexi]+temppara2[indexi]*float(10)       #parası = elindeki para + yatırdığı paranın 10 katı
        masaparasi=masaparasi-temppara2[indexi]*float(10)                 # kazabdığı parayı masa parasından çıkarma
    print(paralar)
    for x in paralar:
        if x<1000:
            paralar[paralar.index(x)]=0
    for (i,j) in zip(adlar,temppara):
        print(i,j)
    
    tur=tur+1
    p=p+1

    if winner(paralar)==1:
        paralar[indexi]=temppara[indexi]+temppara2[indexi]*float(10)
        print("oyun bitti kazanan: ",enzenginkisi)
        print("\n\n\n#########################################################")
        print("#                     ŞANSLI SAYI:",sans,"                  ##")
        print("#########################################################")
        print("#########################################################")
        print("#                          Tur:",tur, "                     ##")
        print("#                                                      ##")
        print("#            MASA BAKİYESİ:",masaparasi,"             ##")
        print("#------------------------------------------------------##")
        print("#                        OYUN BİTTİ..                  ##")
        print("#                   kazanan: " + enzenginkisi +"         ",end = ' ')
        for x in range(18-len(enzenginkisi)): print(" ",end='')
        print("##\n#                PARASI:  ",max(paralar)   ,"          ##")
        print("#                                                      ##")
        print("#                                                      ##")
        print("#########################################################")
        break
    elif winner(paralar)==0:
        print(temppara2)
        
        print("\n\n\n#########################################################")
        print("#                   Bu Turda herkes elendi....             ##")
        print("#                     ŞANSLI SAYI:",sans,"                  ##")
        print("#########################################################")
        print("#########################################################")
        print("#                          Tur:",tur, "                     ##")
        print("#                                                      ##")
        print("#            MASA BAKİYESİ:",masaparasi,"             ##")
        print("#-----------------------------------------------------##")
        encok=max(temppara2)
        enzengin=adlar[temppara2.index(encok)]
        print("#           En çok parası olan:",enzengin,"            ##")
        print("##                PARASI:  ",max(temppara)   ,"          ##")
        print("#                                                      ##")
        print("#                                                      ##")
        print("#########################################################")
        break
    
    print("\n\n\n#########################################################")
    print("#                   ŞANSLI SAYI:",sans,"                    ##")
    print("#########################################################")
    print("#########################################################")
    print("#                                                      ##")
    print("#                      Tur:",tur, "                         ##")
    print("#                                                      ##")
    print("#            MASA BAKİYESİ:",masaparasi,"            ##")
    print("#------------------------------------------------------##")
    print("#             EN ZENGİN KİŞİ: " + enzenginkisi +"                ##")
    print("#                     PARASI:  ",max(paralar)   ,"                ##")
    print("#                                                      ##")
    print("#                                                      ##")
    print("#########################################################")
    
    time.sleep(1)
    os.system('cls')

