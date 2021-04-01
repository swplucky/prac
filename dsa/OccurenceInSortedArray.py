def occurenceInsortedArray(ar,x):
    n = len(ar)
    i = first(ar,0,n-1,x,n)
    if i == -1:
        return i
    j = last(ar,i,n-1,x,n)
    return j-i+1


def first(ar,start,end,x,n):
    if start <= end:
        mid = (start+end)//2
        '''this breaking condition is important
        if mid reaches first element or mid -1 is not same'''
        if (mid == 0 or x > ar[mid-1]) and ar[mid] == x:
            return mid
        if x < ar[mid]:
            return first(ar,0,mid-1,x,n)
        else:
            return first(ar,mid+1,end,x,n)
    return -1


def last(ar,start,end,x,n):
    if start <= end:
        mid = (start+end)//2
        if (mid == n-1 or x < ar[mid+1]) and ar[mid] == x:
            return mid
        if x < ar[mid]:
            return last(ar,0,mid-1,x,n)
        else:
            return last(ar,mid+1,end,x,n)
    return -1


if __name__ == '__main__':
    ar = [3,6,7,7,7,8]
    x = 7
    print(occurenceInsortedArray(ar,x))
