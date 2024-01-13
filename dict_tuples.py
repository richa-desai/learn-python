'''
1. We have following information on countries and their population (population is in crores),
Country 	Population
China 	143
India 	136
USA 	32
Pakistan 	21

    i. Using above create a dictionary of countries and its population
    ii. Write a program that asks user for three type of inputs,
    a. print: if user enter print then it should print countries with their population in format,
        china==>143
        india==>136
        usa==>32
        pakistan==>21

    b. add: if user input add then it should further ask for a country name to add.
    If country already exist in our dataset then it should print that it exist and do nothing.
    If it doesn't then it asks for population and
    add that new country/population in our dictionary and print it
    c. remove: when user inputs remove it should ask for a country to remove.
    If country exist in our dictionary then remove it and
    print new dictionary using format shown above in (a). Else print that country doesn't exist!
    d. query: on this again ask user for which country he or she wants to query.
    When user inputs that country it will print population of that country.

    2. You are given following list of stocks and their prices in last 3 days,
    Stock 	Prices
    info 	[600,630,620]
    ril 	[1430,1490,1567]
    mtl 	[234,180,160]
        i. Write a program that asks user for operation. Value of operations could be,
            a. print: When user enters print it should print following,

            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33

            b. add: When user enters 'add', it asks for stock ticker and price.
            If stock already exist in your list (like info, ril etc) then 
            it will append price to the list. Otherwise it will create new entry in your dictionary.
            For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

    3. Write circle_calc() function that takes radius of a circle as
    an input from user and then it calculates and returns area, circumference and diameter.
    You should get these values in your main program by calling circle_calc and then print them
'''
def circle_calc(radius):
    ''' calulate '''
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    diameter = 2 * radius
    return [area, circumference, diameter]

def stock_func():
    ''' stock '''
    stock_name_price = {"info":[600,630,620], "ril":[1430,1490,1567], "mtl":[234,180,160]}
    action = input("Enter action: ")
    if action == "print":
        for stock, prices in stock_name_price.items():
            print(f"{stock} ==> {prices}")
    elif action == "add":
        stock_name = input("Enter stock name: ")
        stock_price = input("Enter stock price: ")
        if stock_name in stock_name_price:
            stock_name_price[stock_name] = stock_name_price[stock_name].insert(stock_price)
        else:
            stock_name_price[stock_name] = [stock_price]
    elif action == "remove":
        stock_name = input("Enter stock name: ")
        del stock_name_price[stock_name]
    else:
        print("Not a valid action")

def driver():
    ''' driver '''
    population = { "China" : 143, "India" : 136, "USA" : 32, "Pakistan" : 21}
    action = input("Enter action: ")
    if action == "print":
        for country, count in population.items():
            print(country, "==>", count)
    elif action == "add":
        country = input("Enter country: ")
        if country in population:
            print("Already count exists")
        else:
            new_country_population = input("Enter population: ")
            population[country] = new_country_population
    elif action == "remove":
        country = input("Enter country: ")
        del population[country]
    else:
        print("Not a valid action")

    stock_func()

    print(circle_calc(7))

driver()
