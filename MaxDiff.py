## Calculate maximum difference between arrays

def maxDiff(a):
    diff=0
    maxdiff=a[1]-a[0]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j]<a[i]:
                maxdiff=max((a[i]-a[j]),maxdiff)
    return maxdiff      