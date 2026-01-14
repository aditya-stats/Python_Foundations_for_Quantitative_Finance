#Exmple of for loop
profits = [10, -5, 20, -2, 15]
total_profit = 8

for p in profits:
    print("Daily Profits:", p)
    total_profit = total_profit + p

print("Total Profit:", total_profit)

#Example of while loop
returns = [5, -2, 3, -1, 4]

i = 2
total = 10

while i < len(returns):
    total += returns[i]
    i += 1

print("Total Return:", total)

#Example of range() function
for i in range(1, 6):
    print(i, "square is", i**2)

#Example of using break and continue statements
returns = [5, 7, -2, 6, -15, 8]
profits = []

for r in returns:
    if r < -10:
        print("Major loss, exiting loop.")
        break

    if r <= 0:
        continue

    profits.append(r)

print("Profitable days:", profits)