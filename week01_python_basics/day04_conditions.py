#Example of using if statement
price = 180
discount = 20
if price >= 180:
    print("You are eligible for a discount of", discount, "units")


#Example of using else statement
buy_price = 100
sell_price = 108

if sell_price > buy_price:
    print("Trade resulted in PROFIT")
else:
    print("Trade resulted in LOSS")

#Example of using elif statement
if sell_price > buy_price:
    print("Profit")
elif sell_price < buy_price:
    print("Loss")
else:
    print("Break-even")

#Example of nested if statement
SHIB_price = 100
PEPE_price = 200
sell_price = 108

if SHIB_price < PEPE_price:
    if sell_price > SHIB_price:
        print("SHIB is cheaper and sell price is higher than SHIB price")
    else:
        print("SHIB is cheaper but sell price is lower than SHIB price")
else:
    if sell_price > PEPE_price:
        print("PEPE is cheaper and sell price is higher than PEPE price")
    else:
        print("PEPE is cheaper but sell price is lower than PEPE price")

#Example of using and logical operator
if sell_price > PEPE_price and sell_price < SHIB_price:
    print("Sell price is higher than PEPE but lower than SHIB prices")

#Example of using or logical operator
if sell_price < PEPE_price or sell_price > SHIB_price:
    print("Sell price is either lower than PEPE or higher than SHIB prices")
else:
    print("Sell price is neither lower than PEPE nor higher than SHIB prices")

#Example of using not logical operator
if not (sell_price < buy_price):
    print("The trade did not result in a loss")

nse = "OPEN"
if not (nse == "CLOSED"):
    print("NSE is open for trading today")

#Example of using nested logical operators
if not (sell_price < buy_price) and not (sell_price > buy_price):
    print("The trade resulted in a break-even")
else:
    if sell_price > buy_price or sell_price == buy_price:
        print("The trade resulted in either a profit or a break-even")
    else:
        print("The trade resulted in a loss")