#vending machine
print("SELECT A NUMBER FROM THE MENU")
print("-------------------------------------")
print("\t 1.COFFEE")
print("\t 2.TEA")
print("\t 3.MILK")
print("\t 4.BLACK COFFEE")
print("\t 5.GREEN TEA")
print("--------------------------------------")
s_no = int(input("Enter a number from menu : "))

if s_no<1 or s_no>5 :
    print("'SORRY!!!'We are not offering that much service")
else :
    if s_no==1 :
        print("Do you want COFFEE.......?")
        cost_1=int(input("PLEASE PAY 10 RUPEES FOR COFFEE : "))
        if cost_1==10 :
            print("Enjoy with your COFFEE")
        else :
            print("You have not paid sufficient amount")
    elif s_no==2 :
        print("Do you want TEA......?")
        cost_2=int(input("PLEASE PAY 10 RUPEES FOR TEA : "))
        if cost_2==10 :
            print("Enjoy with your TEA")
        else :
            print("You have not paid sufficient amout")
    elif s_no==3 :
        print("Do you want MLIK......?")
        cost_3=int(input("PLEASE PAY 20 RUPEES FOR MILK : "))
        if cost_3==20 :
            print("Enjoy with your MILK")
        else :
            print("You have not paid sufficient amout")
    elif s_no==4 :
        print("Do you want BLACK COFFEE.....?")
        cost_4=int(input("PLEASE PAY 50 RUPEES FOR BLACK COFFEE : "))
        if cost_4==50 :
            print("Enjoy with your BLACK COFFEE")
        else :
            print("You have not paid sufficient amout")
    elif s_no==5 :
        print("Do you want GREEN TEA")
        cost_5=int(input("PLEASE PAY 50 RUPEES FOR GREEN TEA : "))
        if cost_5==50 :
            print("Enjoy with your GREEN TEA")
        else :
            print("You have not paid sufficient amout")
    else :
        print("-----------THANKS FOR VISITING-----------")