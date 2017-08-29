
def ekok_bulma(a,b):

    i = 2
    result = 1

    while (True):
        if(a%i == 0 and b%i ==0):
            result *= i
            a = a // i
            b = b// i
        elif(a%i == 0 and b%i !=0):
            result *=i
            a //=i
        elif(a%i != 0 and b%i ==0):
            result *=i
            b //=i
        else:
            if (a == 1 and b == 1):
                break
            else:
                i+=1
    return result

print(ekok_bulma(12,24))