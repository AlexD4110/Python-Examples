# Map
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Filter
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]

# Reduce (requires import from functools in Python 3.x)
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120
