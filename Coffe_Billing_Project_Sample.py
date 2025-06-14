import datetime
user_name=input("enter the User name :")
Qty=int(input("How many tea you want : "))
cost=10
amount=cost*Qty
cgst=2.5/100
sgst=2.5/100
amount_cgst=amount*cgst
amount_sgst=amount*sgst
total_amount=amount+amount_cgst+amount_sgst

print("\n\n")
print("\t  sweets & snacks pvt ltd")
print("  CF203, sector1, saltlake, kolkata-700064")
print("\t    ph : 033-69000005")
print("\t GST IN:19AADCG7132K1ZE")
print("\t      BILL")
print("------------------------------------------------------")
print("   Memo# 17/41840\t ",datetime.datetime.now())
print("   User : {}\t\t\tPax# 1".format(user_name))
print("\t\t  Order# 1")
print("------------------------------------------------------")
print("Product\t\t\tQty\t Rate\tAmount")
print("------------------------------------------------------")
print(" Tea\t\t\t{}\t {}\t{}".format(Qty,cost,amount))
print("------------------------------------------------------")
print("Sub Total \t\t\t\t{}".format(amount))
print("C Gst @ 2.5%\t\t\t\t",amount_cgst)
print("S Gst @ 2.5%\t\t\t\t",amount_sgst)
print("------------------------------------------------------")
print("Total\t Qty : {}\t\tAmt\t{} \n".format(Qty,total_amount))
print("Thank You , Please Visit again")