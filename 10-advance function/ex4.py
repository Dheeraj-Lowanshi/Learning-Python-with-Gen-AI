def grocery(name, price):
    print("item is",name,",It's price",price)

grocery("Bread", price=20) #keyword can appear after positional argument
grocery(price=250, "Butter") #keyword argument cannot appear before positional argument
