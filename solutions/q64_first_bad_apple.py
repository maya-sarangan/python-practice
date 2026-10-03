def first_bad_apple(apples):
    for i in range(len(apples)):
        if apples[i] == "rotten":
            return i
    return -1
