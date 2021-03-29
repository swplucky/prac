def subsetSum(target,value,n,partial):
    if target==0:
        return partial
    if n==0:
        return []
    if value[n-1]>target:
        return subsetSum(target,value,n-1,partial)
    else:  # list append works on references but + creates new list
        return subsetSum(target-value[n-1],value,n-1,partial + [value[n-1]]) or \
        subsetSum(target,value,n-1,partial)

if __name__ == '__main__':
    s = [6,4,7,3]
    sum = 11
    partial = []
    print(subsetSum(sum,s,len(s),partial))