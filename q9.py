speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
k=list(speed.values())
temp=[]
for i in k:
    if i in temp:
        k.remove(i)
    temp.append(i)
print(k)