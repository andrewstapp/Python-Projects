total_cost_of_food = float(input('How much did the food cost? '))
sales_tax = 8.25
tax_plus_total = total_cost_of_food * sales_tax / 100 
print("Your tax for this meal was:", tax_plus_total)
print("Would you like to add a tip? ")
answer_1 = input("a)Yes\nb)No\n")
if answer_1.lower() == "b" or answer_1.lower() == "no" or answer_1 == "No" or answer_1 == "B":
    print('Thanks for dining with us, your total is:', tax_plus_total + total_cost_of_food)

else:
    print("Nice! How much would you like to tip? ")
    tipammount = float(input("How much would you like to tip? (in dollars)"))
    print(tipammount)
    print("Thanks for dining with us today, your total is:", tax_plus_total + tipammount + total_cost_of_food)


