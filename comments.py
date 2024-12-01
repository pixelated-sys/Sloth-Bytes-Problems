def isValid(string):
    if len(string)%2 != 0 :
        return False
    stack = []
    valid = ["/*","*/","//"]
    for i in range(0,len(string)-1,2):
        a = string[i]+string[i+1]
        if a not in valid:
            return False
        if (a=="/*" or a=="//"):
            stack.append(a)
        elif (a=="*/"):
            if stack[-1] == "/*":
                stack.pop()
            else:
                return False
    if(stack == [] or "//" in stack):
        return True
ans = isValid("/////")
print(ans)