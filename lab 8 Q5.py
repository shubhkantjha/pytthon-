set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Update set1 with items from set2, except common items
set1.update(set2 - set1)
print("set1 after update:", set1)
