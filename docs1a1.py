a={"a":2,"b":3,"c":7,"d":6,}
b={"e":6,"f":9,"g":4,"h":8}
d={}
for i in a:
    for j in b:
        d[i]=a[i]
        d[j]=b[j]               
print(d)
