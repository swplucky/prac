def arraySum(arr):
    n = len(arr)
    l = [0]*n
    r = [0]*n
    for i in range(1,n):
        l[i] = l[i-1]+arr[i-1]
    for j in range(n-2,-1,-1):
        r[j] = r[j+1]+arr[j+1]
    for k in range(0,n):
        arr[k] = l[k] + r[k]
    return arr

if __name__ == '__main__':
    ar = [3,5,6,7,7]
    print(arraySum(ar))