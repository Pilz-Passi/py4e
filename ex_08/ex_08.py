han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    if line == "":   
        continue
    wds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != "From":
        continue
    print(wds[2])