### String expansion --> 3[a2[b]]-> abbabbabb

def stringExpansion(s):
    stackNum=[]
    stackStr=[]
    removeTill=""
    s1=""
    for char in s:
        if char.isdigit(): stackNum.append(int(char))
        elif char == '[': removeTill=char
        elif char ==']':
            num = stackNum.pop()
            c=""
            while c!=removeTill and stackStr:
                c = stackStr.pop()
                s1=c+s1
            while num>1:
                s1+=s1
                num-=1
        else:
            if removeTill=='[':removeTill=char
            stackStr.append(char)
    print(s1)
    return s1
stringExpansion("3[a2[bc]]")
    