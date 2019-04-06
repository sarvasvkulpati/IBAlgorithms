#======== Selection Sort ==========


array = [1, 5, 3, 86, 256, 420, 9, 510, 51, 24, 60]

for i in range(0, len(array)):
    minimum_element_index = i
    for j in range(i + 1, len(array)):
        if array[minimum_element_index] > array[j]:
            minimum_element_index = j
    temp = array[i]
    array[i] = array[minimum_element_index]
    array[minimum_element_index] = temp

print("Sorted elements:")

for i in range(0, len(array)):
    print(array[i])