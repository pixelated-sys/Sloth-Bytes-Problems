def bucket(sent,n):
    l = []  
    s = sent.split()
    i = 0
    while i < len(s):
        e = s[i]
        i += 1
        while (i<len(s)) and len(e)+len(s[i])+1 <= n:
            e += ' ' + s[i]
            i += 1
        l.append(e)
    print(l)

bucket("she sells sea shells by the sea",10)
bucket("the mouse jumped over the cheese", 7)
bucket("fairy dust coated the air",20)
bucket("a b c d e", 2)