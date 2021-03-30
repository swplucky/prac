def missingNumber(ar):
    total= 1
    missingSum = 0
    for i in range(2,len(ar)+2):
        total += i
        missingSum += ar[i-2]
    return total - missingSum

if __name__ == '__main__':
    print(missingNumber([1,3,4,5]))