#Algoritmalar Practice 1:


a=input("Lütfen bir sayı giriniz?")
if a.isdigit():
    if int(a) in [0,1,2,3,4,5,6,7,8,9]:
        sonuc=int(a) + int(a*2) + int(a*3)
    else:
        sonuc="Lütfen geçerli bir sayı giriniz"
else:
    sonuc="Lütfen Geçerli bir sayı giriniz"

print(sonuc)