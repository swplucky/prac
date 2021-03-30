def towerOfHanoi(n,frm,to,aux):
    if n==1:
        print("dist 1 from %s rod to %s rod" % (frm,to))
        return
    towerOfHanoi(n-1,frm,aux,to)
    print("dist %s from %s rod to %s rod" % (n,frm,to))
    towerOfHanoi(n-1,aux,to,frm)

if __name__ == '__main__':
    towerOfHanoi(3,'A','B','C')