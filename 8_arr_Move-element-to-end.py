
#***Time --> O(n) --> as we traverse through the whole array
#***Space --> O(1) --> as we are sorting the array in place nd not using any additional space

def moveElementToEnd (array, toMove):
    i = 0 
    j = len(array) - 1
    while i < j:
        while i < j and array[j] ==toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 3
print(moveElementToEnd(array, toMove))