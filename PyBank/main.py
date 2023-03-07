import csv

with open('Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)

    # Skip header row
    next(csvreader)

    # Initialize variables
    total_months = 0
    net_profit_loss = 0
    prev_profit_loss = 0
    profit_loss_changes = []
    months = []

    # Loop through rows in csvreader
    for row in csvreader:
        # Count number of months
        total_months += 1

        # Add profit/loss to net total
        net_profit_loss += int(row[1])

        # Calculate profit/loss change and add to list
        profit_loss_change = int(row[1]) - prev_profit_loss
        profit_loss_changes.append(profit_loss_change)

        # Save current profit/loss for next loop iteration
        prev_profit_loss = int(row[1])

        # Save month for each row
        months.append(row[0])
        # Calculate average profit/loss change
average_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find greatest increase in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase) ]

# Find greatest decrease in profits
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease) ]

# Formating the values to currency string 
net_profit_loss_formatted = "${:,.2f}".format(net_profit_loss)
greatest_increase_formatted = "${:,.2f}".format(greatest_increase)
greatest_decrease_formatted = "${:,.2f}".format(greatest_decrease)
average_profit_loss_change_formatted = "${:,.2f}".format(average_profit_loss_change)

# Print results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss_formatted}")
print(f"Average Change: {(average_profit_loss_change_formatted)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_formatted})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease_formatted})")

# Print results in txt file
with open("Analysis/financial_analysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: {net_profit_loss_formatted}\n")
    txt_file.write(f"Average Change: {average_profit_loss_change_formatted}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_formatted})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease_formatted})\n")