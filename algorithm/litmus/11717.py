from collections import deque

def aTrans(input_list):
    first_line = input_list[0], input_list[1], input_list[2], input_list[3]
    second_line = input_list[7], input_list[6], input_list[5], input_list[4]

    input_list[0], input_list[1], input_list[2], input_list[3] = second_line
    input_list[7], input_list[6], input_list[5], input_list[4] = first_line

    return input_list

def bTrans(input_list):
    return [input_list[3]] + input_list[0:3] + input_list[5:7] + [input_list[7]] + [input_list[4]]

def cTrans(input_list):
    input_list[1], input_list[2], input_list[5], input_list[6] = input_list[2], input_list[5], input_list[6], input_list[1]

    return input_list

def dTrans(input_list):
    input_list[0], input_list[4] = input_list[4], input_list[0]

    return input_list

def bfs(input_list, target_list):
    if input_list == target_list:
        return 0
    
    queue = deque([(input_list, 0)])
    visited = set()

    trans_alpha_list = ['a', 'b', 'c', 'd']
    trans_typ_list = [aTrans, bTrans, cTrans, dTrans]
    
    while queue:
        current_list, depth = queue.popleft()

        if tuple(current_list) in visited:
            continue
        else:
            visited.add(tuple(current_list))

        counted = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        previous_alpha = None

        for trans_alpha, trans_type in zip(trans_alpha_list, trans_typ_list):
            if trans_alpha == previous_alpha:
                counted[trans_alpha] += 1
            else:
                counted[trans_alpha] = 1

            previous_alpha = trans_alpha

            if (trans_alpha == 'a' or trans_alpha == 'd') and counted[trans_alpha] == 2:
                counted[trans_alpha] = 0  
                depth -= 2
                continue  
            
            if (trans_alpha == 'b' or trans_alpha == 'c') and counted[trans_alpha] == 4:
                counted[trans_alpha] = 0  
                depth -= 4
                continue 

            trans_list = trans_type(current_list.copy())

            if trans_list == target_list:
                return depth + 1
            else:
                queue.append((trans_list, depth + 1))
    
if __name__ == '__main__':  
    init_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    target_list = list(input().split(' '))

    result = bfs(init_list, target_list)
    print(result)
