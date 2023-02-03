def Linearserch (L,s):
    c=0
    j=0
    for i in L:
        if i == s:
            print("position of",s,"is",j)
            c=1
            j
        if c == 0:
            print ("not found")
L=[10,20,30,40,50,60]
s=30
Linearserch(L, s)
