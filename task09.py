import json
import xml.etree.ElementTree as ET
import yaml


def to_format(form=None):
    def decorator(func):
        def wrapped(*args):
            temp = func(*args)
            
            if form == 'xml':
                root = ET.Element('root')
                ET.SubElement(root, 'text').text = str(temp)
                result = ET.tostring(root)
                print(result)
                return result     
                   
            elif form == 'yaml':
                result = yaml.dump(temp)
                print(result)
                return result
            
            else:
                result = json.dumps(temp)
                print(result)
                return result
            
        return wrapped
    return decorator


@to_format()
def return_text():
    return "Hello, World!"


@to_format()
def return_list():
    return ["World", "Planets", "Countries", "Cities"]


@to_format()
def return_dictionary():
    return {1: "a", 2: "b", 3: "c", 4: "d"}


return_text()
return_list()
return_dictionary()
