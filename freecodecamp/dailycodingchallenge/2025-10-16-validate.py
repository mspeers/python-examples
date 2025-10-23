

import re

def validate(email):
    if (email[0] == '.'):
        return False
    
    find = re.match(r"([\w.-]+)@([A-Za-z0-9!.]+)\.([a-z|A-Z]{2,})", email)
    if (find == None):
        return False

    print("Item 1:"+find.group(1)[-1:])
    
    if (find.group(1)[-1:] == '.'):
        return False



    print(find.groups())

    if (find.group(2)[-1:] == '.'):
        return False

    return (find != None)


if __name__ == "__main__":
    print   (validate("example@test.c0") )
    print   (validate("hello@world..com"))
    print   (validate("develop.ment_user@c0D!NG.R.CKS"))


