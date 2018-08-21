def binary_search(array, value):
    """
    declares the variable of mid, which finds the minimum and maximum of a
    list and divides by 2.
    the array will be iterated through based on the length of the array.
    if the value is equal to the index, then return it. if the value is less
    than the index, divide in two. if the value is greater than the index,
    add the variable plus the mid. if value is not found, return -1.
    """
    max = len(array) - 1
    min = 0

    for x in range(min, (len(array))):
        mid = ((min + max) // 2)

        if array[mid] == value:
            return mid

        if array[mid] > value:
            max = mid + 1

        if array[mid] < value:
            min = mid - 1

    return -1
