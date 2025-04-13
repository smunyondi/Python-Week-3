def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Please enter the original price of the item: "))
    discount = float(input("Now enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Print the result
    if discount >= 20:
        print(f"DISCOUNT ADDED! Final Price: {final_price:.2f}")
    else:
        print(f"NO DISCOUNT! Final Price: {original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the price and discount percentage.")
