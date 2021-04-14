def lcs(word1,word2,m,n):
    if m == 0 or n == 0:
        return 0
    elif word1[m-1] == word2[n-1]:
        return lcs(word1,word2,m-1,n-1) + 1
    else:
        return max(lcs(word1,word2,m,n-1),lcs(word1, word2, m-1,n))

if __name__ == '__main__':
    word1 = 'sdfgadfgddffddfgggffffggggf'
    word2 = 'dfsddf' #searches and ignores for these characters one by one
    print(lcs(word1,word2,len(word1),len(word2)))