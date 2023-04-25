def shorten_to_date(long_date):
    print(long_date)
    short_date = long_date[:long_date.rfind(",")]
    print(short_date)
    return short_date

shorten_to_date("Monday February 2, 8pm")
print(shorten_to_date)
shorten_to_date("Tuesday May 29, 8pm")
print(shorten_to_date)
