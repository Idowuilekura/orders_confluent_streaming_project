import re
from typing import Tuple

def read_log(log_file:str) -> Tuple:
    with open(log_file) as f:
        contents = f.read()
        pattern = r"key\s*=\s*(\S+)\s*value\s*=\s*({.*?}})"

        matches = re.findall(pattern, contents)

        for key, value in matches:
            print("Key:", key)
            print("Values:", value)
            print()
            print(type(value))

            # If you want to convert the dictionary string to a Python dictionary
            value_dict = eval(value)
            # print("Values as dictionary:", value_dict)
        return key, value_dict
    
