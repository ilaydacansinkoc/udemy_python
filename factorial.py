fact = int(input("Kaç faktoriyel?"))
result = 1
while(fact > 0):
    result = result*fact
    fact-=1
    if(fact <= 0):
        print(result)
        break