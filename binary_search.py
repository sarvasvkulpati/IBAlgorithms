#======== Binary Search ==========


array         = [11, 12, 15, 16, 112, 118, 123, 145] #needs to be a sorted array
value_to_find = 15           # your search value
min_index     = 0
max_index     = len(array) - 1
mid_index     = 0
found         = False
value_index   = 0

while found == False and min_index <= max_index:
    mid_index = (min_index + max_index) / 2
    if array[mid_index] == value_to_find:
        found = True
        value_index = mid_index
    
    elif value_to_find > array[mid_index]:
        min_index  = mid_index + 1
    
    else:
        max_index = mid_index - 1

if found == True:
    print(str(value_to_find) + " found at " + str(value_index))
else:
    print(str(value_to_find) + " was not found")