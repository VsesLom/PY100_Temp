Salary = 5000  # зарплата
Spend = 6000  # траты
Months = 10  # количество месяцев
Increase = 0.03  # рост цен

# Оформить решение
def money_for_life(salary, spend, months, increase):
    need_money = 0
    for i in range(1, months + 1):
        need_money += (salary - spend)
        spend += spend * increase  # траты в следующем месяце
    if need_money < 0:
        need_money *= -1

    return need_money

print(round(money_for_life(Salary, Spend, Months, Increase)))
