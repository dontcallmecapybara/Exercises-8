import json


def to_json(func):
    def wrapped(*args):
        temp = func(*args)
        result = json.dumps(temp)
        print(result)
    return wrapped


@to_json
def to_dictionary(keys, values):
    dictionary = dict(zip(keys, values))
    return dictionary


@to_json
def to_list(text):
    result = text.split()
    return result


@to_json
def to_reverse_text(text):
    lst = text.split()
    lst.reverse()

    res_text = ''
    for word in lst:
        res_text += word + ' '

    return res_text


num1 = ["a", "b", "c"]
num2 = [1, 2, 3]
txt = 'My name is Vasya!'

to_dictionary(num1, num2)
to_list(txt)
to_reverse_text(txt)
