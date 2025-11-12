

import re 
'''HTML Tag Stripper

Given a string of HTML code, remove the tags and return the plain text content.

    The input string will contain only valid HTML.
    HTML tags may be nested.
    Remove the tags and any attributes.

For example, '<a href="#">Click here</a>' should return "Click here".

'''
def strip_tags(html):
    start_tag = None
    new_html = html
    for index, char in enumerate(html):
        # print("Checking:"+char)
        if (char == '<'):
            print("- Found <:"+ str(index) )
            start_tag = index
            # if (start_tag > 0 ):
            #     start_tag -= 1
        elif (char == '>'):
            if start_tag == None:
                continue
            end_tag = index
            if (end_tag < len(html) ):
                end_tag += 1
            print("- Found >:"+ str(end_tag) )

            #remove tag
            print("Start_tag:"+str(start_tag))
            new_html = html[0:start_tag] + html[end_tag:]
            print("new HTML: "+new_html)
            start_tag = None
            new_html = strip_tags(new_html)

    return new_html
if __name__ == "__main__":
    print("Results:"+strip_tags('<a href="#">Click here</a>')) 


'''
1. strip_tags('<a href="#">Click here</a>') should return "Click here".
2. strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
3. strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
4. strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.'''



