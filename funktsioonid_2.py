from random import *

from math import *

#try:
#    c = float(input("�mberm��t? "))
#    if c>0:
#        D =round (c/pi,2) 
#        print(f"Puu l�bim��t = {D}") #Puu l�bim��du arvutamine
#    else:
#        print("c peab olema suurem kui 0")
#except:
#    print("Andmet��p on vale")

#try:
#    N=float(input("side 1?"))
#    M=float(input("side 2?"))
#    if M>0 and N>0:
#        D=round(sqrt(N**2+M**2)),2
#        print(f"ristk�liku diagonaal = {D}") #Arvutage Pythoni k�sureal
#    else:
#        print("Viga!")
#except:
#    print("ristk�liku diagonaalon vale")

#try:
#    aeg = float(input("Mitu tundi kulus s�iduks? "))
#    teepikkus = float(input("Mitu kilomeetrit s�itsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus = teepikkus / aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h") #Leidke j�rgnevast n�iteprogrammist semantiline viga:
#    else:
#       print ("Viga!")
#except:
#   print ("Viga!")

#try:
#    a=int(input("number 1?"))
#    b =int(input("number 2?"))
#    c =int(input("number 3?"))
#    d =int(input("number 4?"))
#    e =int(input("number 5?"))
#    if a>0 and b>0 and c>0 and d>0 and e>0:
#        arv = a+b+c+d +e
#        arv = arv/5 
#        print(f"keskmine: = {arv}") #Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 t�is arvus
#    else:("Viga!")
#except:
#    print("viga")


#print("   @..@   ")
#print("  (----)") 
#print(" ( \__/ )") 
#print(' ^^ "" ^^ ') #Joonista samasugune konn

#a=randint(0,100)
#b =randint(0,100)
#c =randint(0,100)
#print(f"a={a}\nb={b}\nc={c}")
#P = a+b+c
#print(f"kolmnurga �mberm��t = {P}") #(P=a+b+c)

#p= randint(1,6)
#summa=(12.9*1.1)/p 
#print(f"{p}-st, Iga�ks maksab {summa}") #Pitsa

#try:
#    print("k�ttusekulu arvutamine")
#    l=float(input("k�tuse liitride kogus: "))
#    km=float(input("L�nitud kilomeetrid:" ))
#    if l>0 and km>0:
#        kuulu = round((l/km)*100),2
#        print(f"kuulu :{kuulu}") #K�tusekulu arvutamine 
#    else:
#        print("Viga!")
#except:
#    print("Viga!")

#try:
#    M=int(input("minutid: "))
#    if M>0:
#        M=M/60
#        tee=M*29,9
#        print(f"J�ulab {tee} km") #Rulluisutajad
#    else:
#        print("viga")
#except:
#    print("Viga!")

#try:
#    print("Ajatesindus")
#    M=int(input("Siseta aja minutites"))
#    if M>0: #1h=60min
#        H=M//60 #h
#        M=M%60  #m
#        print(f"{H}:{M}") #Ajateisendus
#    else:
#        print("Viga!")  
#except:
#    print("Viga!")

print("Ema roobot")
grade = (input("Mis hind on?"))
if grade.isdigit() and int(grade)>0 and int(grade)<=5:
    grade=int(grade)
    if grade == 0:
        print("See on halb hinnang")
    elif grade== 1:
        print("See on halb hinnang")
    elif grade== 2:
        print("See on halb hinnang")
    elif grade== 3:
        print("See on normaalne hinnang")
    elif grade== 4:
        print("See on hea hinnang")
    elif grade== 5:
        print("See on v�ga hea hinnang")
else:
    print("Sa valesti vastas")
