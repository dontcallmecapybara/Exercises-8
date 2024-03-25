import json


json_list = input()
lst = json.loads(json_list)

print(sorted(lst, key=lambda x: x[1], reverse=True))
