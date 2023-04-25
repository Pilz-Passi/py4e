sh = input("Enter hours: ")
sr = input("Enter rate: ")
try: 
    fh = float(sh)
    fr = float(sr)
except: 
    print("Fehler, bitte geben Sie eine Zahl ein")
    # 2nd attempt
    sh = input("Enter hours: ")
    sr = input("Enter rate: ")
    # manual loop
    try:
        fh = float(sh)
        fr = float(sr)
    except: 
        print("Zweites mal falsch. Programm wird beendet.")
        quit()
if fh > 40 :
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)