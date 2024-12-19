# Greedy, 멀티탭 스케줄링
# 하나씩 플러그를 빼는 최소의 횟수를 출력하라

import sys

def findMin(N, order_arr):
    power_strip = []
    switch_ctr = 0

    for i, item in enumerate(order_arr):
        if item in power_strip:
            continue

        if len(power_strip) < N:
            power_strip.append(item)
            continue
        
        remove_idx = -1
        last_idx = -1
        remain_items = set(order_arr[i+1:])
        for p, p_item in enumerate(power_strip):
            if p_item not in remain_items:
                remove_idx = p
                break
            else:
                next_idx = order_arr.index(p_item, i+1)
                if next_idx > last_idx:
                    last_idx = next_idx
                    remove_idx = p

        power_strip[remove_idx] = item
        
        switch_ctr += 1

    return switch_ctr

if __name__ == '__main__':
    # answer = 2
    # inputs = [
    #     '2 7\n',
    #     '2 3 2 3 1 2 7'
    # ]

    inputs = sys.stdin.readlines()

    N, K = map(int, inputs[0].split())
    order_arr = [int(val) for val in inputs[1].split()]

    print(findMin(N, order_arr))