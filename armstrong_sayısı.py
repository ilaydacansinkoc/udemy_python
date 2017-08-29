arms=int(input("Sayıyı giriniz"))
temp=arms
result = 0
while (temp > 0):

    basamak = temp % 10
    result += basamak ** 4
    temp = temp // 10

if(result == arms):
    print("Armstrong Sayısı")
else:
    print("Armstrong Sayısı değil.")