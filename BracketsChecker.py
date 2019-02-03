### Check for brackets

def checkBrackets(s):
    lst=[]
    previousBracket = ""
    for char in s:
        if char == "{" or char == "(" or char == "[" and len(lst)>=0:
            lst.append(char)
            previousBracket = char
        elif previousBracket == "[" and char == "]" or previousBracket == "(" and char == ")" or previousBracket == "{" and char == "}" and len(lst)>0:
            lst.pop();
            if len(lst)>0: 
                previousBracket = lst[len(lst)-1]
        else:
            return False
            
    if len(lst)==0:
        return True
    else:
        return False
    
print(checkBrackets("{([()])}{}[()]"))