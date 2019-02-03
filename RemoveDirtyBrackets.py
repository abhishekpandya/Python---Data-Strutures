## Removes dirty brackets

def removeDirtyBrackets(st):
    stackB=[]
    stackIndex=[]
    for i in range(len(st)):
        if len(stackB)==0 and st[i]==')': stackIndex.append(i)
        
        elif st[i]=='(':
            stackB.append(st[i])
            stackIndex.append(i)
        
        elif st[i]==')':
            stackB.pop()
            stackIndex.pop()
            
    if len(stackB)==0:
        return st
    else:
        while len(stackIndex)>0:
            i=stackIndex.pop()
            st = st[:i]+""+st[i+1:]
    return st

print(removeDirtyBrackets("(abc))))(a(()"))
## Output: (abc)a())