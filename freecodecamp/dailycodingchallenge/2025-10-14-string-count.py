

import re 

def count(text, parameter):
    # items = re.findall(parameter,text,overlapped=True)
    items = re.findall(r'(?=('+parameter+"))",text)
    print(items)
    return len(items)


if __name__ == "__main__":
    print(count('abcdefg', 'def'))
    print(count('101010101010101010101', '101'))



