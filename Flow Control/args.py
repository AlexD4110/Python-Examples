
def add(*Yuh):
    sum = 0
    Yuh = list(Yuh)
    Yuh[0] = 0
    for i in Yuh:
        sum += i
    return sum
print(add(1,2,3,4,4,3,2))