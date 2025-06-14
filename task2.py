
a=[0,1,2,3,4,5,6,7,8,9,10]
# in list element we find out midle element Divisble 5 print "NTR" 
#from the Backword Direc take only odd indexing then add it all  odd indexes after adding if that number exctly divisble by 2 then print "NBK"
#In Frontword direct take indexing which is exctly divisble by 3 and then multiple that numbers if number is more than 3 digit number then print "Hari Krishna"

middle_element=(11//2)
print(a[middle_element])
some_odd=a[-1]+a[-3]+a[-5]+a[-7]+a[-9]+a[-11]
print(some_odd)
mul_odd=a[0]*a[3]*a[6]*a[9]
if a[middle_element] % 5 == 0:
    print("NTR")
elif a[some_odd] %2 ==0:
    print("NBK")
elif mul_odd>999:
    print("HariKrihna")
    
    
    
    
    #How to find 
    
    #Given number is >=10 & number is <=99 
    # 1  2   3   4   == 
     # 1  2   3   4   5
     
     #5//2 =2(cosent)
     #5%2=1(Remainder )   # Cosent+Remainder = middle number index.
     #middle number index -1  #Because index value starting 0 that's why we are subtracting 1 .
     