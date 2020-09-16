import csv

count_records = 0
financial_months = []
monthly_income = []
month_profit = []
with open ('budget_data.csv','r') as financial_data:
    record_reader = csv.reader(financial_data)
    header = next(record_reader)
    for row in record_reader:
        count_records += 1
        financial_months.append(row[0])
        monthly_income.append(int(row[1]))
    for i in range(len(monthly_income)-1):
        month_profit.append(monthly_income[i+1]-monthly_income[i])
        #month_profit.append(monthly_income[i+1]+monthly_income[i])
Average = round(sum(month_profit)/len(month_profit),2)
max_value = max(month_profit)
min_value = min(month_profit)
    
print("Financial Analysis")
print("------------------")
print(f'Total Months: {count_records}')
print(f'Total:{sum(monthly_income)}')
print(sum(month_profit))
print(max_value)
#print(min_value)
print(Average)


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {count_records}')
print(f'Total:{sum(monthly_income)}')
print(sum(month_profit))
print(f"max_value)
#print(min_value)
print(f'Average Change:{Average}")