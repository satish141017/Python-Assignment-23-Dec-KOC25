# Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dict1={}

for i,j in sample_dict.items():
    for k in keys:
        if k==i:
            dict1[i]=j

print(dict1)