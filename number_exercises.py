''' QUESTIONS 
1. You have a football field that is 92 meter long and 48.8 meter wide.
Find out total area using python and print it.
2. You bought 9 packets of potato chips from a store.
Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17
'''
def driver():
    ''' all solutions'''
    length = 92
    width = 48.8
    area = length * width
    print("area:", area)

    packets = 9
    packet_cost = 1.49
    ans = 20 - (packets * packet_cost)
    print("change:", ans)

    bathroom_area = 5.5 ** 2
    ans2 = 500 * bathroom_area
    print("cost in rupees:", ans2)

    print("binary:", bin(17))

driver()
