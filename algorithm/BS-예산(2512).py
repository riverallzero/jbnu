# Binary Search, 예산
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다. 
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 
#    상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

import sys

def calCap(datas, budget):
    if sum(datas) <= budget:
        return max(datas)
    else:
        datas.sort()

        low_money, high_money = min(datas[0], budget // len(datas)), datas[-1]

        while low_money <= high_money:
            std_money = (low_money + high_money) // 2

            sum_money = 0
            for data in datas:
                sum_money += min(std_money, data)
            
            if sum_money <= budget:
                low_money = std_money + 1
            else:
                high_money = std_money - 1

        return high_money

if __name__ == '__main__':
    # answer = 127
    # inputs = [
    #     '4\n',
    #     '120 110 140 150\n',
    #     '485'
    # ]

    inputs = sys.stdin.readlines()

    datas = list(map(int, inputs[1].split()))  
    budget = int(inputs[-1]) 

    print(calCap(datas, budget))