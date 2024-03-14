intersection = lambda list1, list2: list(filter(lambda x: x in list2, list1))

print(intersection([10,11,12,13,14,15], [14, 15, 16, 17, 18]))  