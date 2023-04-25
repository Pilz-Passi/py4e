def six_toast(num):
    diff = num - 6
    if diff >= 0:
        return diff
    else:
        return diff * -1

result = six_toast(15)
print(result)
result = six_toast(6)
print(result)
result = six_toast(3)
print(result)