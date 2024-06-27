# Iterator
nums = [1, 2, 3]
iter_nums = iter(nums)
print(next(iter_nums))  # Output: 1
print(next(iter_nums))  # Output: 2

# Generator
def squares(n):
    for i in range(n):
        yield i ** 2

sq_gen = squares(5)
print(list(sq_gen))  # Output: [0, 1, 4, 9, 16]
