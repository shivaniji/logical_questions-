a={"a":65,"v":45,"e":87,"b":76}
b={}
for i in a:
    for j in a:
        if a[i]<a[j]:
            s=a[i]
            a[i]=a[j]
            a[j]=s
print(a)


# a={"4":6,"5":3,"3":7,"2":1,"1":7}
# d={}
# for i in (a):
#     b=sorted(a.items())
#     d.update(b)
# print(d)


# a={"3":7,"2":6,"5":1}
# for i in a:
#     for j in a:
#         if i>j:
           
        
            
# print(a)