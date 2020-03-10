# Recall
numbers = [13, 4, 18, 35]
# Instead of: filter(lambda num: num % 5 == 0, numbers), we can do
div_by_5 = [num for num in numbers if num % 5 == 0]

print(div_by_5) # [35]

# We can manage the combined case as well:
# Instead of: 
# map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))
arbitrary_numbers = [num ** 3 for num in range(1, 21) if num % 3 == 0]
print(arbitrary_numbers) # [27, 216, 729, 1728, 3375, 5832]