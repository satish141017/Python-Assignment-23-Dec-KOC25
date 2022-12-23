sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
k="location"
for i,j in list(sample_dict.items()):
    if i=="city":
        sample_dict[k]=j
print(sample_dict)