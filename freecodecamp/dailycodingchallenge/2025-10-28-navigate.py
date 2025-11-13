

'''
Navigator

On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

    You always start on the "Home" page, which will not be included in the commands array.
    Valid commands are:
        "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
        "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
        "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.

For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
'''
def navigate(commands):
    cur_place = ["Home"]
    index = 0
    for movement in commands:
        if "Visit" in movement:
            place = movement.replace("Visit ", '',1)
            cur_place.append(place)
            index += 1
        if "Back" == movement and (index-1) >= 0:
            index -= 1
        if "Forward" == movement and (index+1) < len(cur_place):
            index += 1
            


    return cur_place[index]


if __name__ == "__main__":
    print(navigate(["Visit About Us", "Back", "Forward"]))
    print(navigate(["Forward"]))
    print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))

'''
1. navigate(["Visit About Us", "Back", "Forward"]) should return "About Us".
2. navigate(["Forward"]) should return "Home".
3. navigate(["Back"]) should return "Home".
4. navigate(["Visit About Us", "Visit Gallery"]) should return "Gallery".
5. navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) should return "Home".
6. navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) should return "Contact".
7. navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) should return "Visit Us".
'''



