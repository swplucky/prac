def longestPallindrome(string):
    #ls = ''.join(string) string is already a char array
    n = len(string)
    table = [[False for x in range(n)] for y in range(n)]
    start = 0
    maxLength = 1
    i=0
    while i<n:
       table[i][i] = True
       i +=1

    i = 0
    while i<n-1:
        if string[i] == string[i+1]:
            table[i][i+1]=True
            start = i
            maxLength = 2
        i +=1

    k =3
    while k<=n:
        i = 0
        while i<(n-k+1):
            j= i+k-1
            if table[i+1][j-1] and string[i]==string[j]:
                table[i][j]=True
                if k>maxLength:
                    start = i
                    maxLength = k
            i += 1
        k +=1

    print(table)
    return maxLength

if __name__ == '__main__':
    st = 'asdlfkjasdkfsdfsfsajfds'
    print(longestPallindrome(st))