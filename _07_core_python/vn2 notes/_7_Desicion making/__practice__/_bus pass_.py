# Bus pass

# Requirement: deluxe pass = 1190
# metro pass = 1090
# ordinary pass = 990
# student pass = 650

x = int(input("Enter the amount :"))
if x < 649 or x >= 1191:
    print("Enter valid amount",)
if x >= 1190:
    print("Deluxe pass")
    print("Remaining Change:", x - 1190)
elif x >= 1090:
    print("Metro express pass")
    print("Remaining Change:", x - 1090)
elif x >= 990:
    print("ordinary pass")
    print("Remaining Change:", x - 990)
elif x >= 650:
    print("student pass")
    print("Remaining Change:", x - 650)
else:
    print("no pass")
