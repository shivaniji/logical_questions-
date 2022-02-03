a={"a":2,"b":4,"c":5}
b={"d":4,"e":8,"f":2}
for i in a:
    for j in b:
        if a[i]==b[j]:
            if b[j]==a[i]:
                # d.update(a[i],b[j])
                print(a[i],b[j])
        


