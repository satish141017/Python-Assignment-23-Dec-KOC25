first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
inter=first_set & second_set
list1=[]
print(inter)
for i in first_set:
    if i not in inter:
        list1.append(i)
print("Intersection is  ",set(list1))
