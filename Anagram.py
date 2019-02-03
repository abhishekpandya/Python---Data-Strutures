### Anagram

def isAnagram(self, s, t):
    d1={}
    d2={}
    for s1 in s:
        if s1 in d1:
            d1[s1]+=1
        else:
            d1[s1]=1
    for s2 in t:
        if s2 in d2:
            d2[s2]+=1
        else:
            d2[s2]=1
    for key, val in d2.items():
        if key in d1 and len(d1)==len(d2):
            if d2.get(key)!=d1.get(key):
                return False
        else:
            return False
    return True