def decorator(func):
    def wrapped(arg):
        result = func(arg)
        print(result)
        return result
    return wrapped


@decorator
def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res


lst = [1, 2, 3, 4, 5]

multiply(lst)
