

import re

'''
HTML Attribute Extractor

Given a string of a valid HTML element, return the attributes of the element using the following criteria:

    You will only be given one element.
    Attributes will be in the format: attribute="value".
    Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
    Return attributes in the order they are given.
    If no attributes are found, return an empty array.

'''
def extract_attributes(element):
    result = []
    print("Search html:"+ str(element))
    pat = "<([\w]+)\s([-\"=\w\s]*)[\s/]*>"
    elements = re.search(pat,element)
    if (elements == None):
        print("FAILED - Nothing elements. element:"+element+", pat:"+pat)
        return result
    
    inner_elements = elements.group(2)
    print("Search Items:"+ str(elements.group(2)))

    print ("inner_elements:"+str(inner_elements))

    attribes = re.findall("([\w]+=\"[-\w\s0-9]+\")",inner_elements)
    if (elements == None):
        return result
    print ("attribes:"+str(attribes))

    for attribe in attribes:
        #parse attribe
        print ("attribe:"+attribe)
        attributes = re.findall("([\w]+)=\"([-\w\s]*)\"", attribe)
        print ("Attributes:"+str(attributes))
        attributes_join = ", ".join([str(s) for s in attributes[0]])
        print("attributes_join:"+attributes_join)
        result.append(attributes_join)
    


    return result

if __name__ == "__main__":
    print   (extract_attributes('<meta charset="UTF-8" />'))
    print   (extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))


