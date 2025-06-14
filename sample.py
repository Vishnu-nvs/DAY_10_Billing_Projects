a=750
b=0b11111 #7
c=750
d=0b111 #1+2+4+0+16=-23
e=750
#find out the bigger number

# big_number=max(a,b,c,d,e)
# print("the bigger number is :",big_number)


if a>b and a>c and a>d and a>e:
    #T and F and T and F =F
    print("A is bigger")
elif  b>c and b>d and b>e:
    #F and T and F ==F
    print("B is bigger")
elif  c>d and c>e:
    #T and F =F
    print("C is bigger")
elif  d>e:
    #F =F
    print("D is bigger")
else:
    print("E is bigger")

    
