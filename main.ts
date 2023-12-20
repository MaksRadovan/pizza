let Subtotal = 0
let Ingredients = 0
game.splash("Let's calculate the total cost.")
let diameter = game.askForNumber("What is the diameter of your pizza?")
let HST = 0.13
let Labour_Cost = 0.75
let Rent = 1
Ingredients = Rent + (Labour_Cost + Ingredients * diameter)
let Total = Rent + (Labour_Cost + 0.5 * (diameter * 1.13))
game.splash("The cost of the pizza with diameter" + diameter + "cm, and Rent " + Rent + ", with Labour Cost, " + Labour_Cost + " additionally with the Ingredient cost, " + Ingredients + "For a subtotal of " + Subtotal + "." + "With tax, the total will be " + Total + ".")
