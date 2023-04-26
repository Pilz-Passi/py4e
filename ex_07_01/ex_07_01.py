fh = open("mbox-short.txt")
for lx in fh:
    ly = lx.rstrip()
    if ly.startswith("From:") and ly.endswith(".edu"):
        print(ly)