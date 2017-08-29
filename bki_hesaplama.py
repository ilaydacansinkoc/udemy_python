# Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

# BKİ 18.5'un altındaysa -------> Zayıf

# BKİ 18.5 ile 25 arasındaysa ------> Normal

# BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

# BKİ 30'un üstündeyse -------------> Obez

boy = float(input("Boyu giriniz"))
boy = boy / 100
kilo = float(input("Kiloyu giriniz"))

beden_kitle = kilo / (boy * boy)

if (beden_kitle < 18.5):
    print("Zayıf")
elif (beden_kitle >= 18.5 and beden_kitle < 25):
    print("Normal")
elif (beden_kitle >= 25 and beden_kitle < 30):
    print("Fazla Kilolu")
else:
    print("Obez")