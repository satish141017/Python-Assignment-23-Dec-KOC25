first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
def finding_subset(f1set,f2set):
    temp=0
    for i in f2set:
        if i in f1set:
            temp+=1
    if temp==len(f1set):
        return True
    else:
        return False
print("First set is subset of second set ",finding_subset(first_set,second_set))
print("second set is subset of first set ",finding_subset(second_set,first_set))
def finding_superset(f1set,f2set):
    temp=0
    for i in f1set:
        if i in f2set:
            temp+=1
    if temp==len(f1set):
        return True
    else:
        return False
print("first set is superset of secod set ",finding_subset(second_set,first_set))
print("secod set is superset of first set ",finding_subset(first_set,second_set))
