



# What is the score?
score = int(input("What is your test score?\n"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else: 
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('your grade is a D.')
            else:
                print('Your grade is an F.')

counties_dict = {"Araphoe": 422829, "Denver": 463353, "Jefferson": 432438}
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Araphoe" in counties or "El Paso" in counties:
    print("Araphoe and El Paso are in the list of counties.")
else:
    print("Araphoe or El Paso are not in the list of counties.")

for county, i in counties_dict.items():
    print(county, i)

for county, voters in counties_dict.items():
    print(county + " has " + voters + " registered voters")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

for county_dict in voting_data:
    for value in county_dict.values(): 
       print(value)

for county, voters in counties_dict.items():
   print(f"{county} has {voters:,} registered voters")

for county, voters in voting_data():
    print(f"{county} county has {voters:,} registered voters")


import datetime as dt

# use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()

#print the present time
print("The time right now is ", now)

dir(dt)




