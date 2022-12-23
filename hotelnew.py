def hotel_menu():
    global li
    global le
    global dict
    dict={}
    print(" THE HOTEL ITEMS ARE: ")
    while True:
        item=input("enter item:")
        cost=int(input("enter cost of item:"))
        if item=="0" and cost==0:
            break
        else:
            dict.setdefault(item,cost)
    
    li=list(dict.keys())
    le=list(dict.values())
    print(" THE HOTEL MENU :")
    print("----------------------------------------------")
    print("ITEM".rjust(10)+"COST".rjust(28))
    print("----------------------------------------------")
    for x,y in dict.items():
       print(" ".rjust(5," "),end="")
       print(str(x).ljust(15),end="")
       print(str(y).rjust(15),end="")
       print("/-")
    print("----------------------------------------------")        

def Bill():
    global bill
    global bill1
    bill={}
    bill1=[]
    global n
    n=int(input("ENTER YOUR NO'OF ORDERS:"))
    for i in range(n):
        order=input("enter your order:")
        quantity=int(input("enter quantity:"))
        a=le[i]*quantity
        B=str( le[i] )+" * " + str( quantity )+" = "+str(le[i]*quantity)
        if order in li[0]:
            bill.setdefault(li[0],B)
            bill1.append(a)
        elif order in li[1]:
            bill.setdefault(li[1],B)
            bill1.append(a)
        elif order in li[2]:
            bill.setdefault(li[2],B)
            bill1.append(a)
        elif order in li[3]:
            bill.setdefault(li[3],B)
            bill1.append(a)
        elif order in li[4]:
            bill.setdefault(li[4],B)
            bill1.append(a)
        elif order in li[5]:
            bill.setdefault(li[5],B)
            bill1.append(a)
        elif order in li[6]:
            bill.setdefault(li[6],B)
            bill1.append(a)
        elif order in li[7]:
            bill.setdefault(li[7],B)
            bill1.append(a)
        elif order in li[8]:
            bill.setdefault(li[8],B)
            bill1.append(a)
        elif order in li[9]:
            bill.setdefault(li[9],B)
            bill1.append(a)
        elif order in li[10]:
            bill.setdefault(li[10],B)
            bill1.append(a)
        elif order in li[11]:
            bill.setdefault(li[11],B)
            bill1.append(a)
        elif order in li[12]:
            bill.setdefault(li[12],B)
            bill1.append(a)
    return bill
    return bill1
print(" WELCOME TO THE HOTEL..! ")
hotel_menu()
CUSTMER_NAME=input("ENTER CUSTOMER NAME:")
PHONE_NUMBER=int(input("ENTER CUSTOMER PHONE NO:"))
BILL_NO=int(input("enter bill no:"))
Bill()
print(" THE BILL DETAILS ARE :")
print("--------------------------------------------------------")
print("NAME:",end="")
print(CUSTMER_NAME,end="           ")
print("PHONE_NUMBER:",PHONE_NUMBER)
print("\n")
print("BILL_NO:",BILL_NO)
print("--------------------------------------------------------")
print("ITEM".rjust(10)+"COST".rjust(33))
print("--------------------------------------------------------")
for x,y in bill.items():
    print(" ".rjust(5," "),end="")
    print(str(x).ljust(20),end="")
    print(str(y).rjust(20),end="")
    print("/-")
print("--------------------------------------------------------")        
                 
TOTAL=sum(bill1)
print(" ".rjust(3),end="")
print("TOTAL:".ljust(40),end="")
print(TOTAL,end="")
print("/-")
print("--------------------------------------------------------")
print("THANK YOU..! VISIT AGAIN")
