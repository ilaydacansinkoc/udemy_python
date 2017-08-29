sayı = int(input("Sayıyı giriniz.."))
temp = 0
for i in range(1,sayı):
    if(sayı % i == 0):
        temp += i
        if(temp == sayı):
            print("Mükemmel Sayı")
        else:
            print("Mükemmel Değil")