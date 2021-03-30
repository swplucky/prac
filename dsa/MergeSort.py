def mergeSort(ar):
    if len(ar)>1:
        mid= len(ar)//2
        l=ar[:mid]
        r=ar[mid:]
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                ar[k] = l[i]
                i += 1
            else:
                ar[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            ar[k] = l[i]
            i += 1
            k +=1

        while j < len(r):
            ar[k] = r[j]
            j += 1
            k += 1

if __name__ == '__main__':
    ar = [5,3,6,2]
    mergeSort(ar)
    print(ar)