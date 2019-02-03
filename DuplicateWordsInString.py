### Find Duplicate between strings

def findDuplicateWords(raw,query):
    d={}
    lst ={}
    queryStr = query.split(" ")
    for item in queryStr:
        d[item] = queryStr.index(item)
    rawStr = raw.split(" ")
    for item in rawStr:
        if item not in d:
            lst[item] = rawStr.index(item)
    print(lst)
findDuplicateWords("hi there","hi how are you")