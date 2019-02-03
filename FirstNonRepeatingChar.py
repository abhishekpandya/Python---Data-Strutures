# Returns first non repeating character in a string

def firstNonRepeatingChar(s):
    d={}
    for char in s:
        if char in d: d[char]+=1
        else: d[char]=1
    for key,val in d.items():
        if val==1: return key
    return "No items"
    
firstNonRepeatingChar("GeeksGeeks")