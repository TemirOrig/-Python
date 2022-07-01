import re


with open('text_7.txt', 'r', encoding='utf-8') as f:
    com_profit = {}
    av_prof = {}
    com_list = [com_profit, av_prof]
    sum_profit = 0
    i = 0
    for line in f:
        key = line.strip().split(' ')[0]
        value = re.findall('\d+', line)
        value = [int(el) for el in value]
        profit = value[0] - value[1]
        if profit > 0:
            com_profit[key] = profit
            sum_profit += profit
            i += 1
        else:
            com_profit[key] = abs(profit)
    av_prof['average_profit'] = sum_profit / i
    print(com_list)
