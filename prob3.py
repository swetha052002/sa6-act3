def find_max(list1, compare):
  max_value = list1[0]
  for num in list1[1:]:
    max_value = compare(max_value, num)

  return max_value

compare = lambda a, b: a if a > b else b

list1 = [124,42,356,35,4]
maximum = find_max(list1, compare)
print(f"The maximum number in the list is: {maximum}")