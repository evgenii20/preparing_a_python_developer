"""
lesson 1: hw 5
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию
должна передаваться фиксированная ежемесячная сумма пополнения вклада. Считаем,
что клиент вносит средства в последний день каждого месяца, кроме первого и
последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""

# Процентная ставка депозита
interest_rate_deposit = [
    {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
    {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
    {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
]


def get_deposit(start_sum, deposit_term: int, month_sum=0):
    """Функция принимает сумму вклада, срок вклада в месяцах, пополнение вклада"""

    total_amount = 0  # вся сумма
    total_amount2 = 0  # вся сумма + доп. мес. сумма
    for deposit in interest_rate_deposit:
        if deposit['begin_sum'] <= start_sum < deposit['end_sum']:
            total_amount = start_sum
            percent = deposit[deposit_term] / 100

            total_amount += start_sum * percent * (deposit_term / 12)
            if month_sum != 0:
                total_amount2 = total_amount
                total_amount2 += (month_sum * percent * (round((deposit_term - 2) / 12, 2))) * (deposit_term - 2)
            # total_amount += start_sum * percent * (deposit_term / deposit[deposit_term])

    return f'Сумма вклада на конец срока: {total_amount}\n' \
           f'Сумма вклада с учетом пополнения: {total_amount2}'


if __name__ in "__main__":
    print(get_deposit(1000, 6, 100))

"""
Результат:
Сумма вклада на конец срока: 1025.0
Сумма вклада с учетом пополнения: 1031.6
"""
