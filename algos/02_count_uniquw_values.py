

#  this was supposed tp ve a two pointer problem
# work thru the Js code bedore and redo it in Py





# proofread

def count_unique_values(input_lst):
    """ Given an lsit, returnthe number of unique elements in the list"""
    
    lst = []
    for i in input_lst:
        if i not in lst:
            lst.append(i)
    return len(lst) 

# Tests:
print(count_unique_values([1,1,1,1,1,2])) # 2
print(count_unique_values([1,2,3,4,4,4,7,7,12,12,13]))    # 7
print(count_unique_values([]))    # 0
print(count_unique_values([-2,-1,-1,0,1]))    # 4

# def count_unique_values(input_lst):
#     # create an empty list
#     lst = []
#     # for each value in the input list
#     for i in input_lst:
#         # if that value is not in the created list
#         if i not in lst:
#             # add i to the lst
#             lst.append(i)
#     # return the length of the list
#     return len(lst) 

#outline / pseudocode
    # create an empty list
    # for each value in the input list
        # if that value is not in the created list
            # add i to the lst
    # return the length of the list

# function countUniqueValues(arr){
    
#    let i = 0;
#    let j = 1;
#    let len = arr.length;

#    if(len === 0){
#        return 0;
#    }

#    while(j < len){
#         if(arr[i] == arr[j]){
#             j += 1;
#         }else{
#             i += 1;
#             arr[i] = arr[j];
#         }
#    }//end while

#    return i + 1;
# }//end countUniqueValues()

# //Tests:
# //console.log(countUniqueValues([1,1,1,1,1,2]) // 2
# //console.log(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]) // 7
# //console.log(countUniqueValues([]) // 0
# //console.log(countUniqueValues([-2,-1,-1,0,1]) // 4

# /*
# Instructions:
# Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.
# */