


def collatzLen(num):
    steps = 1
    while num != 1:
        steps += 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
            ## Can only get bigger at this step
            if num > 1000000:
                ## Failed, no need to calculate further
                return 1
    return steps

def collatzSearch(low, high):
    maxLen = 1
    maxNum = 1
    for i in range(low, high):
        n = collatzLen(i)
        if n > maxLen:
            maxLen = n
            maxNum = i
    return (maxNum, maxLen)

def main():
    print(collatzSearch(1, 1000000))


if __name__ == "__main__":
    main()
    