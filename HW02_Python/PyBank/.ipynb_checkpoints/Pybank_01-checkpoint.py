import csv

total_net = 0
with open ('graded_homework_02-Python_Instructions_PyBank_Resources_budget_data.csv','r') as financial_data:
    record_reader = csv.DictReader(financial_data)
    for row in record_reader:
        print(row)
    
for 'Date','Profit/Losses' in record_reader.items():
    total_net += int(Profit/Losses)
print(total_net)
       #for row in csv.DictReader(financial_data):
            #print(row)
#total_net = 0
#print(row)