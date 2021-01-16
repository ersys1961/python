cnt = 0
sum_salary = 0
with open('test3.txt', 'r', encoding="utf-8") as f_inp:
    for line in f_inp:
        fio, s1 = line.split()
        salary = float(s1)
        cnt += 1
        sum_salary += salary
        if salary < 20000.0:
            print(f'Менее 20 тыс. руб. : {fio}')
avg_salary = round(sum_salary / cnt, 2) if cnt > 0 else 0.0
print(f'Средняя зарплата: {avg_salary}')
