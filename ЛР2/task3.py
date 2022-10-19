Money_capital = 10000
Salary = 5000
Spend = 6000
Increase = 0.05
Spend_before_salary = True  # расходы раньше доходов? Значение может быть только True или False!

# Оформить решение

def how_many_month(money_capital, salary, spend, increase, spend_before_salary):
    month = 0
    all_spend = 0  # переменная для всех расходов
    if spend_before_salary:
        while money_capital > all_spend:
            money_capital += salary  # зарплата в конце текущего месяца
            all_spend += spend
            spend += spend * increase  # расходы на начало следующего месяца
            month += 1
            if money_capital < all_spend + spend:
                break
    else:
        while money_capital > all_spend:
            money_capital += salary  # зарплата в конце текущего месяца
            all_spend += spend
            spend += spend * increase  # расходы за следующий месяц, после получения новой зарплаты
            if money_capital < all_spend:
                break
            else:
                month += 1

    return month

print(how_many_month(Money_capital, Salary, Spend, Increase, Spend_before_salary))
