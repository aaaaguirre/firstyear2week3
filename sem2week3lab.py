# Question 1

weekly_target = []


for i in range(4):
    salesperson = input("Please enter Salesperson Number:")
    daily_sales = input("Please enter your daily sales:")
    weekly_sales = daily_sales * 7
    salesperson_figures = [salesperson, daily_sales]
    weekly_target.append(salesperson_figures)

highest_sales = max(weekly_target)
lowest_sales = min(weekly_target)

print("{0:20}".format("Weekly sales:"))
print("-"*60)
for salesperson_figures in weekly_target:
    for i, information in enumerate(daily_sales):
        if i == 0:
            print("{0:20}".format(information), end="")
        else:
            print("{0:<10}".format(information), end="")
    total_sales = (3 * salesperson_figures[1]) + (1 * salesperson_figures[2])
    print("{0:<10}".format(total_sales))
print("-"*60)
print("Highest sales:", highest_sales, "Lowest sales", lowest_sales)