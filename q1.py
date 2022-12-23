l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_l1=[l1[i] for i in range(len(l1)) if i%2!=0]
even_l2=[l2[j] for j in range(len(l2)) if j%2==0]
print("Element at odd-index positions from list one")
print(odd_l1)
print("Element at even-index positions from list two")
print(even_l2)
for k in even_l2:
    odd_l1.append(k)
print("Printing Final third list")
print(odd_l1)