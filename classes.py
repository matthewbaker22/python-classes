class Pizza:
    def __init__(self, size, crust):
       self.size = size
       self.toppings = []
       self.crust = crust

    def add_topping(self, toppings):
        self.toppings.append(toppings)
    
    def pizza_output(self):
        print(f"I would like a", self.size, "inch", self.crust, "crust pizza with", self.toppings[0], "and", self.toppings[1], ".")

meat_lovers = Pizza(16, "deep dish")
meat_lovers.add_topping("peperoni")
meat_lovers.add_topping("sausage")
meat_lovers.pizza_output()

vegan_pizza = Pizza(12, "thin")
vegan_pizza.add_topping("spinach")
vegan_pizza.add_topping("mushrooms")
vegan_pizza.pizza_output()