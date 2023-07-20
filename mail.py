import datetime as DT
from datetime import date
from turtle import pd


def years_between_dates(pay, sale):
    delta = sale - pay
    return delta.days // 365


data_pay = input('Введите дату приобретения имущества в формате dd/mm/yyyy: ')
pay = DT.datetime.strptime(data_pay, '%d/%m/%Y').date()
# print(pay)
data_sale = input('Введите дату продажи в формате dd/mm/yyyy: ')
sale = DT.datetime.strptime(data_sale, '%d/%m/%Y').date()

years = years_between_dates(pay, sale)  # получил полных лет между датами приобретения и продажи

# print(f'Вы владели имуществом {years} полных года')

if years >= 3:
    print('Поздравляю! Вы владели имуществом более 3 лет, доход освобождается от налогообложения')
else:
    print('Доход подлежит налогообложению')

# запрос расчета налога
accept_calculation = input('Рассчитать налог? (yes/no): ')

if accept_calculation == 'no':
    print('Всего хорошего')
elif accept_calculation == 'yes':
    print('Приступаем')
else:
    print('Пожалуйста введите yes или no и нажмите Enter')
#while accept_calculation  == ('yes', 'no'):

# price_pay = input('Введите сумму затраченную на приобретение имущества: ')
# price_sale = input('Введите сумму полученную от продажи имущества: ')
# calculate_tax = ()