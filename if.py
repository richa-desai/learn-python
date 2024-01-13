'''Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

Write a program that asks user to enter a city name and
it should tell which country the city belongs to

Write a program that asks user to enter two cities and
it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print
"Both cities are in India" but if I enter mumbai and dhaka it should print
"They don't belong to same country"

Write a python program that can tell you if your sugar is normal or not.
Normal fasting level sugar range is 80 to 100.

Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
country_list = [india, pakistan, bangladesh]

city1 = input("city1:")
city1 = city1.lower()
if city1 in india:
    print("India")
elif city1 in pakistan:
    print("Pakistan")
elif city1 in bangladesh:
    print("Bangladesh")
else:
    print("City not in any data")

city2 = input("city2:")
city3 = input("city3:")
for country in country_list:
    if (city2.lower() in country and city3.lower() in country):
        print("Both cities are in", country)
        break
else:
    print("They don't belong to same country")

sugar = input("Please enter your sugar level:")
sugar = float(sugar)
if sugar < 80:
    print("Your sugar is low")
elif sugar > 100:
    print("Your sugar is high")
else:
    print("Your sugar is normal")
