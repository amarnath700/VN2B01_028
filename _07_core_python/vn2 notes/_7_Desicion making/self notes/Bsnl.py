# Bs-nl
print("--Welcome to Bsnl--")
print("commercial = com")
print("institutional = ins")
print("Domestic = dom")
print("---Select category---")
ca = input("category (com, ins, dom):")
if ca == "com":
    print("Thanks for selecting commercial")
    un = int(input(" Please enter how many units you want :"))
    if un <= 5000:
        print("you bill amount : 1500")
    elif 5000 < un <= 10000:
        print("First 5000 units Fixed rate is 1500")
        print("Rs.0.25/unit from 5001 to 10000 units")
        print("you bill amount:", ((un-5000) * 0.25)+1500)
    elif 10000 < un <= 20000:
        print("First 5000 units Fixed rate is 1500")
        print("Rs.0.23/unit from 10001 to 20000 units")
        print("you bill amount:", ((un-5000) * 0.23)+1500)
    else:
        print("First 5000 units Fixed rate is 1500")
        print("Rs.0.20/unit More than 20000 units")
        print("you bill amount:", ((un-5000) * 0.20)+1500)

elif ca == "ins":
    print("Thanks for selecting Institutional")
    un = int(input(" Please enter how many units you want:"))
    if un <= 5000:
        print("you bill amount : 1800")
    elif 5000 < un <= 10000:
        print("First 5000 units  Fixed rate is 1800")
        print("Rs.0.30/unit from 5001 to 10000 units")
        print("you bill amount:", ((un-5000) * 0.30)+1800)
    elif 10000 < un <= 20000:
        print("First 5000 units Fixed rate is 1800")
        print("Rs.0.28/unit from 10001 to 20000 units")
        print("you bill amount:", ((un-5000) * 0.28)+1800)
    else:
        print("First 5000 units Fixed rate is 1800")
        print("Rs.0.25/unit More than 20000 units")
        print("you bill amount:", ((un-5000) * 0.25)+1800)

elif ca == "dom":
    print("Thanks for selecting Domestic")
    un = int(input(" Please enter how many units you want :"))
    if un <= 100:
        print("you bill amount : 75")
    elif 100 < un <= 200:
        print("First 100 units Fixed rate is 75")
        print("Rs.1.25/unit from 101 to 200 units")
        print("you bill amount:", ((un-100) * 1.25)+75)
    elif 200 < un <= 400:
        print("First 100 units Fixed rate is 75")
        print("Rs.2.00/unit from 201 to 400 units")
        print("you bill amount:", ((un-100) * 2.00)+75)
    else:
        print("First 100 units Fixed rate is 75")
        print("Rs.2.50/unit More than 400 units")
        print("you bill amount:", ((un-100) * 2.50)+75)
else:
    print("sorry, yor are selected wrong category")
