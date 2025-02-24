set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Items in set1 that don't exist in set2
set1.update(set1 - set2)
print("Updated set1:", set1)
