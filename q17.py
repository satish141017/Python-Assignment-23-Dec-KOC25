sample_dict = {'a': 100, 'b': 200, 'c': 300}
num=int(input("enter a no."))
if num in sample_dict.values():
    print(num,"present in sample dict")
else:
    print(num,"not present in sample dict")
    