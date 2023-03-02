import csv

with open(r'C:\Users\Fabio_UofT SCS\Desktop\GitHub\python-challenge\PyBank\budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader)  # skip header row

    num_rows = sum(1 for row in reader)
    total = 0
    for row in reader:
        total += int(row[1])
    
    print(f'Total Months:  {num_rows}')
    print(f'Total: ${total}')

    #   ,Profit/Losses