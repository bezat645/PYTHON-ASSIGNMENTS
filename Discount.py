price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percent):
    if 100>discount_percent>=20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

result = calculate_discount(price, discount_percent)
print(result)