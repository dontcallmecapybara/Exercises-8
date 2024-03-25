a = int(input())
b = int(input())
c = int(input())
d = int(input())


result = list(map(lambda x: x % c != 0 and x % 10 == d, range(a, b + 1)))

print(result.count(True))
