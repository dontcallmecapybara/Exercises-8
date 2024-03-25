def is_up(symbol):
    return symbol.isupper()


i = int(input())
j = int(input())
text = list(input())
index_list = [x for x in range(i - 1, j)]

temp_upper_reg = filter(is_up, text)
upper_reg = list(temp_upper_reg)

counter = 0
for item in upper_reg:
    if text.index(item) in index_list:
        counter += 1
        text[text.index(item)] = ' '

print(counter)
