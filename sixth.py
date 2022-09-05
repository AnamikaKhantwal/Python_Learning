house_price = 10000000
credit = int(input("Enter credit"))

if credit>500:
    house_price_new = int(0.1 * house_price)
    print("Downpayment is "+ str(house_price_new))
elif credit<=500:
    house_price_new = int(0.2 * house_price)
    print("Downpayment is "+ str(house_price_new))


