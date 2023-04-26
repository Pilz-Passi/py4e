print("Visit: https://www.codewars.com/users/Pilz-Passi")
while True:
    try:
        h = int(input("Enter Pascals honor points: "))
        break
    except:
        print("Please enter a valid number.")

m = 30 - h

def rank(h):
    if h >= 40:
        print("Milestone reached!")
        print("Current rank: 7 kyu.")
        return print((40 - h) * -1, "points above Milestone.")
    elif h >= 30:
        print("Milestone reached!")
        print("Current rank: 7 kyu.")
        return print("only", 40 - h, "points to the next Milestone.")
    else:
        print("Still missing", m, "points")
        print("Current rank: 8 kyu.")
rank(h)
input("Press Enter to close...")