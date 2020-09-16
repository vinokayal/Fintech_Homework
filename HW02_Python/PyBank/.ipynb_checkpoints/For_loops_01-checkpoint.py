profit = []
num = [10, 20, 30, 40, 50]
for i in range (len(num)-1):
    print(f'i is {i}')
    print(f'num is {num}')
    profit.append(num[i+1]-num[i])
    print(f'Profit is {profit}')