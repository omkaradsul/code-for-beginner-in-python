from array import *
array1 = array('i', [1, 2, 3, 4, 5, 6])
print(array1[2])#for acessing elements
array1.insert(6, 7)#used to insert elements in array
array1.remove(3)#used to remove elements
array1[2] = 3#used to update elements
for x in array1:
    print(x)
