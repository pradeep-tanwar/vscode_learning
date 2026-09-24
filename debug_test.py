def calculate_total(price, quantity):
    total = price * quantity
    discount = total * 0.10
    final_price = total - discount

    return final_price


price = 1000
quantity = 3

result = calculate_total(price, quantity)

print("Final Price:", result)