#======== Bubble Sort ==========


array = [1, 663, 8, 2, 4, 1, 22, 66, 20, 122]

sorting_in_ascending = True

for i in range(0, len(array)-1):
    for j in range(0, len(array)-1 -i):
        if sorting_in_ascending:   
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        else :   
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

print("Sorted elements:")

for i in range(0, len(array)):
    print(array[i])