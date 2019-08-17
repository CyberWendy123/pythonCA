#second project based on CH 4: Lists (Aug 11, 2019)
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizzas = list(zip(toppings, prices))
print(pizzas)

# 7. Sort pizzas so that the pizzas with the lowest prices are at the start of the list.
# 8. Store the first element of pizzas in a variable called cheapest_pizza.
# 9. A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”
# 	Get the last item of the pizzas list and store it in a variable called priciest_pizza.
# 10. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
#	Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.
# 11. Print the three_cheapest list.
# 12. Your boss wants you to do some research on $2 slices.
#	Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out. 