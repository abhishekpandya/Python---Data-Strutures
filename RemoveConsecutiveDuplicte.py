# Removes consecutive duplicates

def removeConsecutiveDuplicte(s):
    p=""
    l=len(s)
    for i in range(l):
        if i<l:
            if p==s[i]: 
                s=s[:i]+s[i+1:]
                l=len(s)
            p=s[i]
    return s