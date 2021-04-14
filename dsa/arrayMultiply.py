def product(ar):
    l = [0 for i in ar]
    r = [0 for i in ar]
    prod = [0 for i in ar]
    n = len(ar)
    l[0] = 1
    r[n-1] = 1

    for i in range(1, n):
        l[i] = ar[i-1] * l[i-1]
    for j in range(n-2, -1, -1):
        r[j] = ar[j+1] * r[j+1]
    for k in range(n):
        prod[k] = l[k] * r[k]

    return prod

if __name__ == '__main__':
    ar = [3,5,2,6,1]
    print(product(ar))