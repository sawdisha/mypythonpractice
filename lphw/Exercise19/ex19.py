def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} chesses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 50)

# default argument
print("Variable definition as a function arugment")
def cheese_and_crackers_again(cheese_cnt = 24, bxs_of_crackers = 30):
    print(f"You have {cheese_cnt} chesses!")
    print(f"You have {bxs_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
cheese_and_crackers_again()
cheese_and_crackers_again(5*2, 7-2)
cheese_and_crackers_again(6/3, 8*2)
cheese_and_crackers_again(amount_of_cheese / 5, amount_of_crackers /2)
cheese_and_crackers_again(amount_of_cheese - 6, amount_of_crackers + 3)
cheese_and_crackers_again(45, 23)
cheese_and_crackers_again(2 * 2 * 2, 4 * 2 * 2)
cheese_and_crackers_again(input("Enter the cheese count: "), input("Enter the cracker box count: "))
cheese_and_crackers_again("Twenty", 'Fourty')
cheese_and_crackers_again(int(input("Enter the count of cheese you just bought: ")) + 2, int(input("Enter the count cracker boxes you just bought: ")) + 3)
