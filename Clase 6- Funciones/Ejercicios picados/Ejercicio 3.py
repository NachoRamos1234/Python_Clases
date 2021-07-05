d={}
for x in range(0,10):
    numero=int(input("Ingrese un numero mayor a 0: "))
    d[x]=numero

def mayor(d):
    max=0
    for x in d.values():
        if (x>max):
            max=x
    return max

def menor(d):
    min=0
    for x in d.values():
        if (x<min):
            min=x
    return min
max=mayor(d)
print(max)
min=menor(d)
print(min)



