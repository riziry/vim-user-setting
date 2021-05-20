import datetime

def MoonAgeCalculator(name, age):
    print(name + "! your moon age is: " + str(age*12))
    now = datetime.datetime.now()
    print("Born in", str(now.year - age))

MoonAgeCalculator("rizqi", 20)

