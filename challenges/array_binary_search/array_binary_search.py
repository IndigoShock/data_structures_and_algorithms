

def binary_search(array, value):
    '''
    declares the variable of mid, which finds the length of the array and divides by 2.
    then the array will be iterated through based on the length of the array. if the value is equal to the index, then return it. if the value is less than the index, divide in two. if the value is greater than the index, add the variable plus the mid. if value is not found, return -1.
    '''
    mid = len(array) // 2
    for index in range(len(array)):

        if value == array[index]:
            return index

        if value < array[index]:
            mid = mid // 2

        if value > index:
            mid = mid + (mid // 2)
            
    return -1
