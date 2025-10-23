

def classification(temp):

    star_types = [
        ["O", 30000, -1],
        ["B", 10000, 29999],
        ["A", 7500, 9999],
        ["F", 6000, 7499],
        ["G", 5200, 5999],
        ["K", 3700, 5199],
        ["M", 0, 3699],
    ]

    for star in star_types:
        if (star[2] == -1 and temp >= star[1]):
            print ("Star:" + str(star) +"")
            return star[0]
        if (star[2] >= temp and star[1] <= temp):
            return star[0]

    return "?"

if __name__ == "__main__":
    print(classification(5778))


