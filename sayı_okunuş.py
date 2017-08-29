onlar = ["On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
birler = ["Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]



def okunus(sayi):
    onlar_bsm = sayi // 10
    birler_bsm = sayi % 10
    return onlar[onlar_bsm-1]+" "+birler[birler_bsm-1]

inpt = int(input("Sayıyı giriniz"))
print(okunus(inpt))