sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
dict2={}
# Keys to remove
keys = ["name", "salary"]
for i,j in sample_dict.items():
    if i in keys:
        pass
    else:
        dict2[i]=j

            
print(dict2)