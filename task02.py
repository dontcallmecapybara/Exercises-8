a = int(input())
b = int(input())
c = int(input())
d = int(input())

interval = [x for x in range(a, b + 1)]

temp_list = filter(lambda x: x % c == 0 and x % d == 0, interval)
fin_list = list(temp_list)

count = 0
for elem in fin_list:
    count += elem

print(count)
