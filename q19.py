sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
k=min(sample_dict.values())
for i,j in sample_dict.items():
    if k==j:
        print(i)