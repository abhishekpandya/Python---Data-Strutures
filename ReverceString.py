## Reverce string

def reverseString(s):
    st = s.split(" ")
    newStr = ""
    for s1 in st[::-1]:
        newStr+= s1+" "
    print(newStr + "\nand length: " + str(len(newStr)))

reverseString("hi how are you")



