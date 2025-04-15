from collections import Counter
def isLongPressed(ori,sticky):
    o = Counter(ori)
    s = Counter(sticky)
    for i in o:
        if o[i] > s[i]:
            return False
    i = 0
    j = 0
    while j<len(sticky):
        if i==len(ori):
            return False
        if(ori[i]==sticky[j]):
            j+=1
            continue
        i+=1
    return True

print(isLongPressed("laiden", "laiden") )
print(isLongPressed("saeed", "ssaaedd"))