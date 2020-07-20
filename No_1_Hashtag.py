def Hashtag(string):
    tag = '#'
    string_split = string.split()
    for i in string_split:
        tag += i.capitalize()

    if len(string) > 140 or string == "":
        return False
    else:
        return tag  

print(Hashtag("Hello there how are you doing"))
print(Hashtag("   Hello    World"))
print(Hashtag(""))