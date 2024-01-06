'''
1. Create 3 variables to store street, city and country,
now create address variable to store entire address.
Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line

2. Create a variable to store the string "Earth revolves around the sun"
        Print "revolves" using slice operator
        Print "sun" using negative index

3. Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where
x and y presents vegetables and fruits that you eat everyday.
Use python f string for this.

4. I have a string variable called s='maine 200 banana khaye'.
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original string with new ones and print the new string.
Also try to do this in one line.
'''
def driver():
    ''' all solutions'''
    street = "Fish market 13"
    city = "Regensburg"
    country = "Germany"
    address = street + '\n' + city + '\n' + country + '\n'
    print("Address using + operator:\n" + address)
    address = f'{street}\n{city}\n{country}'
    print("Address using f-string:\n" + address)

    str1 = 'Earth revolves around the sun'
    print(str1[6:14])
    print(str1[-3:])

    fruits = 10
    vegetables = 5
    print(f"I eat {vegetables} veggies and {fruits} fruits daily")

    str2 = 'maine 200 banana khaye'
    str2 = str2.replace('banana','samosa').replace('200','10')
    print("Using single line:",str2)

driver()
