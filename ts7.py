import json
dct = {}
profit_all = 0.0
cnt = 0
with open('test7.txt', 'r', encoding="utf-8") as f_inp:
    for line in f_inp:
        firm, _, income, costs = line.split()
        profit = float(income) - float(costs)
        if profit > 0:
            profit_all += profit
            cnt += 1
            dct[firm] = profit
    profit_avg = round(profit_all / cnt, 2) if cnt > 0 else 0
    lst = [dct, {'average_profit': profit_avg}]
    with open("test7_1.json", "w", encoding="utf-8") as write_f:
        json.dump(lst, write_f, ensure_ascii=False)

print(lst)
