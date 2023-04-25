def contamination(text, char):
    if char != "" and text != "":
        return len(text) * char
    else: 
        return ""
result = contamination("abc","z")
print(result)
result = contamination("","z")
print(result)
result = contamination("abc","")
print(result)
result = contamination("_3ebzgh4","&")
print(result)
result = contamination("//case"," ")
print(result)