roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
k=sample_dict.values()
for i in roll_number:
    if i not in k:
        roll_number.remove(i)
print("Result after remove   ",roll_number)
