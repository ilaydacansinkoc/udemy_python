a = 1
b = 1
fib = [a,b]
for i in range(11):
    a,b = b, a+b
    fib.append(b)
for j in fib:
    print(j)
