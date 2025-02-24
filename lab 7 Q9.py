my_tuple = (1, 2, 3, 1, 4, 5, 2)
repeated_items = [item for item in set(my_tuple) if my_tuple.count(item) > 1]
print("Repeated Items:", repeated_items)
