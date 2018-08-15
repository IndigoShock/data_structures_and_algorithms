
def insertShiftArray(array, value):
  '''
  inserts value into the middle of the array. if the length is odd, the insertion will be to right of the middle array integer
  '''
  half_length = len(array)//2
  if (len(array) % 2):
      half_length = len(array)//2 + 1
  return (array[:half_length] + [value] + array[half_length:])
