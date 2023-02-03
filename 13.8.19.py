numbers_tickets = int(input('Ввести количество билетов: '))
sum = 0


for i in range(0, numbers_tickets):
    age = int(input('Ввести возраст участника: '))
    if age < 18:
        print('Стоимость билета: 0 руб')
    elif 18 <= age < 25:
        sum += 990
        print('Стоимость билета: 990 руб')
    else:
        sum += 1390
        print('Стоимость билета 1390 руб')


discount = int(sum * 0.9)
if sum > 3:
    print('Стоимость всех приобретаемых билетов со скидкой:', sum, 'руб')
else:
    print('Стоимость всех приобретаемых билетов:', sum, 'руб')










