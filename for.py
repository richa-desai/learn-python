'''
1.After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads

2.Print square of all numbers between 1 to 10 except even numbers

3.Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and
program should tell you in which month that expense occurred.
If expense is not found then it should print that as well.

4.Lets say you are running a 5 km race. Write a program that,
Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message

5.Write a program that prints following shape
*
**
***
****
*****
'''
def driver():
    ''' all soultions '''
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    head_counter = 0
    for outcome in result:
        if outcome == "heads":
            head_counter += 1
    print("Head counter:", head_counter)

    for i in range(1,11):
        if i % 2 != 0:
            print(i*i)

    expense_list = [2340, 2500, 2100, 3100, 2980]
    expense = int(input("Enter expense: "))
    if expense in expense_list:
        i = expense_list.index(expense)
        print(i+1, "is the number of the month for the respective expense")
    else:
        print("Expense not found in the list")

    for j in range(1,5):
        print("You finished", j, "km. Are you tired?")
        response = input()
        if response == "yes":
            print("you didn't finish the race")
            break
        if response == "no":
            continue
    else:
        print("congratulations! You finished 5 km race")

    for k in range(1, 6):
        for _ in range(k):
            print("*", end="")
        print()

driver()
