sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict1={}
for i in sample_list:
    dict1[i]=sample_list.count(i)
print("Printing count of each item   ",dict1)
