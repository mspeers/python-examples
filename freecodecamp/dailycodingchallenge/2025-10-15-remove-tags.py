

import re 

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



