""" does the second list contain the square of each item in the first list."""

#  Sequential loops, O(n)
def same(lst1, lst2):
    # create a dictionary representing lst1 where the keys are the unique elements of lst1 and the values are how often they each occur.
    dct = {}
    for element in lst1:
        if element in dct:
            dct[element] += 1
        else:
            dct[element ] = 1
            
    # if an element in lst2 has it's square root in lst1, decrement the value of that square root/key by 1
    for element in lst2:
        if element ** 0.5 in dct:
            dct[element ** 0.5] -= 1
    
    # if all values in dct are now 0, each elements in lst1 had a natching square in lst2 so the frequencies natch
    
    if all(value == 0 for value in dct.values()) == True:
        return True
    else:
       return False

 
print(same([1, 2, 3], [1, 9, 4]))    # true
print(same([1, 2, 3], [1, 4, 25]))   # false
print(same([1, 2, 3, 4], [1, 4, 15, 16]))    # false
print(same([1, 2, 3, 4], [1, 16, 9, 4]))    # true


# nested loops O(nSquared)
# def same(lst1, lst2):
#     for x in lst1[:]:
#         if  x ** 2 in lst2:
#             lst2.remove(x ** 2)
#             lst1.remove(x)
#     if len(lst1) == 0 and len(lst2) == 0:
#         return True
#     else:
#         return False
# print(same([1, 2, 3], [1, 9, 4]))    # true
# print(same([1, 2, 3], [1, 4, 25]))   # false
# print(same([1, 2, 3, 4], [1, 4, 15, 16]))    # false
# print(same([1, 2, 3, 4], [1, 16, 9, 4]))    # true