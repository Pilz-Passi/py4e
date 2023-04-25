def converter(mpg):
    kpl = float((1.609344 / 4.54609188) * mpg)
    return round(kpl, 2)
   
result = converter(10)
print(result)