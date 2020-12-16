def add(*num):
    total = 0
    for n in num:
        total += n
    print(total)
add(2,3,4,5,6)

def calculate(**kwargs):
    print(type(kwargs))

calculate(add=3, multiply=5)