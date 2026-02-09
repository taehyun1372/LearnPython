def domain_name(url):
    if url.find("www.") != -1:
        index = url.find("www.") + len("www.")
    elif url.find("http://") != -1 :
        index = url.find("http://") + len("http://")
    elif url.find("https://") != -1 :
        index = url.find("https://") + len("https://")
    else:
        index = 0
    url = url[index:]
    index = url.find(".")
    if index != -1:
        url = url[:index]
    return url






if __name__ == "__main__":
    testee1 = "http://google.com"
    testee2 = "http://google.co.jp"
    testee3 = "https://123.net"
    testee4 = "https://hyphen-site.org"
    testee5 = "http://codewars.com"
    testee6 = "www.xakep.ru"
    testee7 = "https://youtube.com"
    testee8 = "http://www.codewars.com/kata/"
    testee9 = "icann.org"

    result1 = domain_name(testee1)
    result2 = domain_name(testee2)
    result3 = domain_name(testee3)
    result4 = domain_name(testee4)
    result5 = domain_name(testee5)
    result6 = domain_name(testee6)
    result7 = domain_name(testee7)
    result8 = domain_name(testee8)
    result9 = domain_name(testee9)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
    print(result8)
    print(result9)
