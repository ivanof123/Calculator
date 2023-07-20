import datetime as DT
from datetime import date
from turtle import pd


def years_between_dates(pay, sale):
    delta = sale - pay
    return delta.days // 365


data_pay = input('Введите дату приобретения в формате dd/mm/yyyy: ')
pay = DT.datetime.strptime(data_pay, '%d/%m/%Y').date()
# print(pay)
data_sale = input('Введите дату продажи в формате dd/mm/yyyy: ')
sale = DT.datetime.strptime(data_sale, '%d/%m/%Y').date()

years = years_between_dates(pay, sale)  # получил полных лет между датами приобретения и продажи

#print(f'Вы владели имуществом {years} gjkys[ года')

# delta = sale - pay
# print(f'Вы владели имуществом {delta.days} дней')