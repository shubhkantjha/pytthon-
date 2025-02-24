sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
updated_list = [sample_list[i] for i in range(len(sample_list)) if i not in [0, 4, 5]]
print("Updated List:", updated_list)
