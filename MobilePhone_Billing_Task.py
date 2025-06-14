import datetime
user_name=input("enter the User name :")
Qty=int(input("How many Mobiles you want : "))
cost=90000
amount=cost*Qty
cgst=2.5/100
sgst=2.5/100
amount_cgst=amount*cgst
amount_sgst=amount*sgst
total_amount=amount+amount_cgst+amount_sgst

if Qty==2:
    Discount=(10/100)*total_amount
elif Qty>=3 and Qty<=5:
    Discount=(15/100)*total_amount
elif Qty>=6 and Qty<=10:
    Discount=(17/100)*total_amount
elif Qty>=11 and Qty<=15:
    Discount=(23/100)*total_amount
elif Qty>=15:
    Discount(25/100)*total_amount
    
    
print("\n\n")
print("\t  VISHNU MOBILES Sales & Services")
print("  1-1,Metro complex,RTC Bustand Road,Madanapalli-517325")
print("\t    Mobile NO:720720720")
print("\t GST IN:13VVDCM1182V1ED")
print("\t      BILL")
print("------------------------------------------------------")
print("   Memo# 03/30033\t ",datetime.datetime.now())
print("   User : {}\t\t\tPax# 03".format(user_name))
print("\t\t  Order# 55")
print("------------------------------------------------------")
print("Product\t\t\tQty\t Rate\tAmount")
print("------------------------------------------------------")
print(" Mobile\t\t\t{}\t {}\t{}".format(Qty,cost,amount))
print("------------------------------------------------------")
print("Sub Total \t\t\t\t{}".format(amount))
print("Discount \t\t\t\t{}".format(Discount))
print("C Gst @ 2.5%\t\t\t\t",amount_cgst)
print("S Gst @ 2.5%\t\t\t\t",amount_sgst)
print("------------------------------------------------------")
print("Total\t Qty : {}\t\tAmt\t{} \n".format(Qty,total_amount))
print("------------------------------------------------------")
print("\nSaved Amount",Discount)
print("\nAfter Discount Amount need to be pay",total_amount-Discount)
print("\nThank You , Please Visit again")