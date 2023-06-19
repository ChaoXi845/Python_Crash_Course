def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


