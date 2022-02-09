import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# car
x = {
    'cars': ["BMW", "Volvo", "Ford"],
    'y': [3, 7, 2]
}

z = pd.DataFrame(x)

print(z)


# cla

my = pd.DataFrame(calories)

print(my)