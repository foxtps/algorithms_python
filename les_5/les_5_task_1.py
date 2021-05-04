from collections import namedtuple
QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarter_profit', 'profit'])
all_company = set()
all_profit = 0
num = int(input('Введите количество организаций: '))
for i in range(1, num+1):
    name = input(f'Введите наименование {i} организации: ')
    profit = 0
    quarter_profit = []
    for j in range(QUARTERS):
        quarter_profit.append(float(input(f'Введите прибыль за {j+1} квартал: ')))
        profit += quarter_profit[j]
    company_data = Company(name, tuple(quarter_profit), profit)
    all_company.add(company_data)
    all_profit += profit

average_profit = all_profit/num
print(f'Компании заработали больше {average_profit} :')
#print([company.name for company in all_company if company.profit > average_profit])
for company in all_company:
    if company.profit > average_profit:
        print(f'{company.name}')
print(f'Компании заработали меньше {average_profit} :')
#print([company.name for company in all_company if company.profit < average_profit])
for company in all_company:
    if company.profit < average_profit:
        print(f'{company.name}')