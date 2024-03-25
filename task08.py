from datetime import datetime


def decorator(func):
    def wrapped(*args):
        filename = 'log.txt'
        try:
            result = func(*args)
            print(result)
        except Exception as error:
            with open(filename, 'a') as f:
                print(datetime.now(), error, file=f)
            print('Error')
    return wrapped


@decorator
def calculation(num_1, num_2):
    result = int(num_1) // int(num_2)
    return result


number = input()
devider = number[-1]

calculation(number, devider)
