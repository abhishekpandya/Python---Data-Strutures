## Generate all binary strings for ex 1?1 -> 101 , 111 ( Replaces ? with 0 and 1)

def binaryStrings(s,index):
    if index==len(s):
        print(s)
        return
    if s[index]=='?':
        s=s[:index]+"0"+s[index+1:]
        completeStrings(s,index+1)
        s=s[:index]+"1"+s[index+1:]
        completeStrings(s,index+1)
    else:completeStrings(s,index+1)

binaryStrings("1??0?101",0)