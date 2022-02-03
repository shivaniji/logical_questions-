a=[3,7,5]
b=[6,3,8]
d={}
for i in a:
    for j in b:
        d[i]=j
        b.remove(j)
        break
print(d)