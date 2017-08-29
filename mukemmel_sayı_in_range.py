def mukemmel(sayi):
    temp = 0

    for i in range(1,sayi):
        if(sayi % i == 0):
            temp += i

    if(temp == sayi):
        return True
    else:
        return False


for i in range(1,1000):
    if(mukemmel(i)):
        print(i)