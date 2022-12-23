sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
temp=[]
for i in sample_list:
    if i in temp:
        sample_list.remove(i)
    temp.append(i)
print(sample_list)
print(tuple(sample_list))
print(max(sample_list))
print(min(sample_list))