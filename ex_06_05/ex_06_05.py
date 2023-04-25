str = 'X-DSPAM-Confidence: 0.8475 '
#print(str)

entry = str.find(":")
#print(entry)

number = str[entry + 1:].strip()
#print(number)

final = float(number)
print(final)