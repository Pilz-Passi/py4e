def count_sheep(n):
    if n == 0:
        return ""
    elif n >= 1: 
        count = 1
        murmur = ""  # initialize a string variable to "None"
        while count < n + 1:  # repeat the loop n times
            counter = str(count)  # convert count to a string
            s = " sheep..."  # define a string that contains the phrase " sheep..."
            murmur = murmur + counter + s  # add the phrase "1 sheep..." to the murmur string
            count = count + 1  # increment the count variable by 1
        return murmur  # return the final murmur string
    return  # return nothing if n is negative

# call the function with different values of n and print the result
result = count_sheep(0)
print(result)

result = count_sheep(1)
print(result)

result = count_sheep(2)
print(result)

result = count_sheep(4)
print(result)
