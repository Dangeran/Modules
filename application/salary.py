# не понимаю, почему не могу подгрузить сюда список, полагаю, что конфликт модулей (не работает main.py)
# from db.people import people_salary
salary = [12000, 12500, 13000, 15000, 17500]


def calculate_salary():
    sum_salary = 0
    for s in salary:
        sum_salary += s
    print(f'Сумма всех окладов работников: {sum_salary}')


if __name__ == '__main__':
    calculate_salary()
