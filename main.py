Subtotal = 0
Ingredients = 0
game.splash("Let's calculate the total cost.")
diameter = game.ask_for_number("What is the diameter of your pizza?")
HST = 0.13
Labour_Cost = 0.75
Rent = 1
Ingredients = Rent + (Labour_Cost + Ingredients * diameter)
Total = Rent + (Labour_Cost + 0.5 * (diameter * 1.13))
game.splash("The cost of the pizza with diameter" + str(diameter) + "cm, and Rent" + str(Rent) + ", with Labour Cost," + str(Labour_Cost) + "additionally with the Ingredient cost's," + str(Ingredients) + "For a subtotal of " + str(Subtotal) + "." + "With tax, the total will be " + str(Total) + ".")