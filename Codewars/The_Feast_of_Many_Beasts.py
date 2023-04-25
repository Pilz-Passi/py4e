def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]: 
        return True
    else: 
        return False
    
result = feast("great blue heron", "garlic naan")
print(result)
result = feast("brown bear", "bear claw")
print(result)