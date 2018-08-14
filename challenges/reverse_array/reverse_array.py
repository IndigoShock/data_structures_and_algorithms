def reverse_array(input_list):
  """Fancy docstring
  """
  for i in range(len(input_list) // 2):
    input_list[i], input_list[i-1] = input_list[i-1], input_list[i]

    return input_list