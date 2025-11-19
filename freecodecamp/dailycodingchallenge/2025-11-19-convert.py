

'''
Markdown Heading Converter

Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

    Start with zero or more spaces, followed by
    1 to 6 hash characters (#) in a row, then
    At least one space. And finally,
    The heading text.

The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
'''
MSG_INVALID_FORMAT = "Invalid format"

def convert(heading, mark="#"):
    start = heading.find(mark)
    if start == -1:
        return MSG_INVALID_FORMAT    
    count = 1
    for index in range(start+1,len(heading)):
        word = heading[index]
        print(f"word:{word}, index:{index}")
        if word == mark:
            count += 1
        elif word == " ":
            break 
        else:
            print("falied missing space after #")
            return MSG_INVALID_FORMAT


    # rule count can biger then 6 
    if count >= 7:
        return MSG_INVALID_FORMAT

    # build string out add one for space. 
    end = count + start + 1
    heading_result = heading[end:].lstrip()
    results = f"<h{count}>{heading_result}</h{count}>"


    return results

'''
1. convert("# My level 1 heading") should return "<h1>My level 1 heading</h1>".
Waiting: 2. convert("My heading") should return "Invalid format".
Waiting: 3. convert("##### My level 5 heading") should return "<h5>My level 5 heading</h5>".
Waiting: 4. convert("#My heading") should return "Invalid format".
Waiting: 5. convert("  ###  My level 3 heading") should return "<h3>My level 3 heading</h3>".
Waiting: 6. convert("####### My level 7 heading") should return "Invalid format".
Waiting: 7. convert("## My #2 heading") should return "<h2>My #2 heading</h2>".
'''

if __name__ == "__main__":
    print(convert("# My level 1 heading")   )
    print(convert("  ###  My level 3 heading"))



