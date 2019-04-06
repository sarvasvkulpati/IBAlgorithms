#======== Sequential Search ==========

array = [2, 9, 5, 6, 7, 8]  # Your array of values
value_to_find = 7           # your search value
found = False               # boolean value
counter = 0                 # we don't need to initialise this here in python but it's a good idea to do so in pseudocode

for counter in range(0, len(array)):    #this line is the same as: loop counter from 0 to array.length - 1
    if array[counter] == value_to_find:
        found = True
        print(str(array[counter]) + " found at " + str(counter)) 
                                        #there's no end if or end loop in python, remember to include it

if found == False:
    print(value_to_find + " not found")