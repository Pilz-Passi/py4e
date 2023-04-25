sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    print("overtime")
else:
    print("regular")
xp = fh * fr
print("Pay:", xp)