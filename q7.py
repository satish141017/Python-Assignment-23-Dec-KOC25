first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
temp=0
for i in second_set:
    if i in first_set:
        temp+=1
if temp==len(first_set):
    print(True)
else:
    print(False)