def missingNumber(ar):
    # i starts from 0 we need to take sum from 1 to n. So include n and 1 from start by range 2 to n+2.
    total= 1
    missingSum = 0
    for i in range(2,len(ar)+2):
        total += i
        missingSum += ar[i-2]
    return total - missingSum

if __name__ == '__main__':
    print(missingNumber([1,2,3,4,5,7]))