dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
b={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i==j==k:
                m=({dic1[i]+dic2[j]+dic3[k]})
b.update({1:10})
b.update({2:20})
b.update({3:30})
b.update({4:40})
b.update({5:50})
b.update({6:60})
print(b)










# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#      if i==j:
#                 m=(dic1[i]+dic2[j])
# b.update({1:10})
# b.update({2:20})
# b.update({j:m})
# b.update({3:30})
# b.update({5:50})
# b.update({6:60})
# print(b)
                
