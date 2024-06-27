def countdown(n):
    while n > 0:
        yield n # return n, but remember the state of the function
        n -= 1

for number in countdown(10):
    print(number)




'''Matters
With yield: The generator yields values one at a time,
allowing the caller to control the iteration process and 
perform actions between yielded values if needed.'''