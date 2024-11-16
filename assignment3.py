def calculateDiscount ():
    price = float(input("Enter the Original price of item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    if discount_percent >= 20:
        discounted_price = price * (discount_percent / 100)
        new_price = price - discounted_price
        print(f"The discount price is: {discounted_price}")
        print(f"The new price after applying the discount is: {new_price}")
    
    else:
        print(f"No discount applied. The original price remains: {price}")
calculateDiscount()
