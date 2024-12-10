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