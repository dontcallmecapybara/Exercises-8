from functools import reduce


a = int(input())
b = int(input())
c = int(input())

interval = [x for x in range(a, b + 1)]

lst = []
for number in interval:
    if (number**0.5).is_integer() and number % c == 0:
        lst.append(number)

result = reduce(lambda x, y: x*y, lst)
print(result)
