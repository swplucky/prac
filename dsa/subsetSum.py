def subsetSum(target,value,n):
    if target==0:
        return True
    if n==0:
        return False
    if value[n-1]>target:
        return subsetSum(target,value,n-1)
    else:
        return subsetSum(target-value[n-1],value,n-1) or \
               subsetSum(target,value,n-1)

if __name__ == '__main__':
    s = [6,4,7,3]
    sum = 11
    print(subsetSum(sum,s,len(s)))