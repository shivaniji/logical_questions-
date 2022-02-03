d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
b={}
for i in (d1):
    for j in (d2):
        if i==j:
            l=d1[i]==d2[j]
            b.update({i:l})
# print(b)
b.update({"d":400})
b.update({"c":300})

print(b)


