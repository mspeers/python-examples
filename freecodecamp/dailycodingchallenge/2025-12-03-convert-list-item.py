

import re
'''
Markdown Ordered List Item Converter

Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

    Start with zero or more spaces, followed by
    A number (1 or greater) and a period (.), followed by
    At least one space, and then
    The list item text.

If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
'''
MSG_INVALID = "Invalid format"

def convert_list_item(markdown):
    items = markdown.split(".")
    items[0] = items[0].lstrip()
    # items[0] = items[0].rstrip()
    print(items)

    matchs = re.match("^\d+$", items[0])
    print(matchs)
    if not matchs or items[0] == "":
        return MSG_INVALID

    items[1] = items[1].lstrip()
    result = f"<li>{items[1]}</li>"
    return result


if __name__ == "__main__":
    print(convert_list_item("1. My item"))
    print(convert_list_item(". invalid again"))
    print(convert_list_item("1 . invalid item"))
'''
1. convert_list_item("1. My item") should return "<li>My item</li>".
2. convert_list_item(" 1.  Another item") should return "<li>Another item</li>".
3. convert_list_item("1 . invalid item") should return "Invalid format".
4. convert_list_item("2. list item text") should return "<li>list item text</li>".
5. convert_list_item(". invalid again") should return "Invalid format".
6. convert_list_item("A. last invalid") should return "Invalid format".
'''



