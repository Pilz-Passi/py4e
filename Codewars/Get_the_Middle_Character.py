def get_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 1: # if lenght has a remainder of 1, it has to be odd
        return s[mid]   # hence only returning one single letter
    else:
        return s[mid-1:mid+1] # return the letter 1 before and 1 after the mid
        

result = get_middle("test")
print(result)
result = get_middle("testing")
print(result)
result = get_middle("middle")
print(result)
result = get_middle("A")
print(result)
result = get_middle("of")
print(result)