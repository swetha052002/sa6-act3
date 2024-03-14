custom_sort = lambda strings: sorted(strings, key=lambda s: (len(s), s))

print(custom_sort(["Red", "green", "blue", "orange", "voilet"]))  