import copy

list1 = ['a','b',1,2,3,True]

list2 = []
for i in list1:
    list2.append(i)
    
print(list2)

list3 = copy.copy(list1)
print(list3)