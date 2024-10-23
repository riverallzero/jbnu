import argparse
import random
import copy
import json
from collections import deque


def rotate_face(face):
    return [face[2], face[0], face[3], face[1]]


def rotate_move(cube, face):
    if face == 'U':
        cube['U'] = rotate_face(cube['U'])

        cube['F'][0], cube['F'][1], cube['R'][0], cube['R'][1], cube['B'][0], cube['B'][1], cube['L'][0], cube['L'][1] = \
            cube['R'][0], cube['R'][1], cube['B'][0], cube['B'][1], cube['L'][0], cube['L'][1], cube['F'][0], cube['F'][
                1]

    elif face == 'D':
        cube['D'] = rotate_face(cube['D'])

        cube['F'][2], cube['F'][3], cube['R'][2], cube['R'][3], cube['B'][2], cube['B'][3], cube['L'][2], cube['L'][3] = \
            cube['L'][2], cube['L'][3], cube['F'][2], cube['F'][3], cube['R'][2], cube['R'][3], cube['B'][2], cube['B'][
                3]

    elif face == 'F':
        cube['F'] = rotate_face(cube['F'])

        cube['U'][2], cube['U'][3], cube['R'][0], cube['R'][2], cube['D'][0], cube['D'][1], cube['L'][1], cube['L'][3] = \
            cube['L'][1], cube['L'][3], cube['U'][2], cube['U'][3], cube['R'][0], cube['R'][2], cube['D'][0], cube['D'][
                1]

    elif face == 'B':
        cube['B'] = rotate_face(cube['B'])

        cube['U'][0], cube['U'][1], cube['R'][1], cube['R'][3], cube['D'][2], cube['D'][3], cube['L'][0], cube['L'][2] = \
            cube['R'][1], cube['R'][3], cube['D'][2], cube['D'][3], cube['L'][0], cube['L'][2], cube['U'][0], cube['U'][
                1]

    elif face == 'L':
        cube['L'] = rotate_face(cube['L'])

        cube['U'][0], cube['U'][2], cube['F'][0], cube['F'][2], cube['D'][0], cube['D'][2], cube['B'][1], cube['B'][3] = \
            cube['B'][1], cube['B'][3], cube['U'][0], cube['U'][2], cube['F'][0], cube['F'][2], cube['D'][0], cube['D'][
                2]

    elif face == 'R':
        cube['R'] = rotate_face(cube['R'])

        cube['U'][1], cube['U'][3], cube['F'][1], cube['F'][3], cube['D'][1], cube['D'][3], cube['B'][0], cube['B'][2] = \
            cube['F'][1], cube['F'][3], cube['D'][1], cube['D'][3], cube['B'][0], cube['B'][2], cube['U'][1], cube['U'][
                3]


# 큐브(cubie) 상태 초기화
cube = {
    'U': ['u1', 'u2', 'u3', 'u4'],
    'F': ['f1', 'f2', 'f3', 'f4'],
    'R': ['r1', 'r2', 'r3', 'r4'],
    'B': ['b1', 'b2', 'b3', 'b4'],
    'L': ['l1', 'l2', 'l3', 'l4'],
    'D': ['d1', 'd2', 'd3', 'd4']
}


# 큐브 상태 전개도 출력
def printCube(cube):
    print('      ┌──┬──┐')
    print('      │{}│{}│'.format(cube['U'][0], cube['U'][1]))
    print('      ├──┼──┤')
    print('      │{}│{}│'.format(cube['U'][2], cube['U'][3]))
    print('┌──┬──┼──┼──┼──┬──┬──┬──┐')
    print('│{}│{}│{}│{}│{}│{}│{}│{}│'.format(cube['L'][0], cube['L'][1], cube['F'][0], cube['F'][1], cube['R'][0],
                                             cube['R'][1], cube['B'][0], cube['B'][1]))
    print('├──┼──┼──┼──┼──┼──┼──┼──┤')
    print('│{}│{}│{}│{}│{}│{}│{}│{}│'.format(cube['L'][2], cube['L'][3], cube['F'][2], cube['F'][3], cube['R'][2],
                                             cube['R'][3], cube['B'][2], cube['B'][3]))
    print('└──┴──┼──┼──┼──┴──┴──┴──┘')
    print('      │{}│{}│'.format(cube['D'][0], cube['D'][1]))
    print('      ├──┼──┤')
    print('      │{}│{}│'.format(cube['D'][2], cube['D'][3]))
    print('      └──┴──┘')


# 목표 큐브(cubie) 상태
goalCube = {
    'U': ['u1', 'u2', 'u3', 'u4'],
    'F': ['f1', 'f2', 'f3', 'f4'],
    'R': ['r1', 'r2', 'r3', 'r4'],
    'B': ['b1', 'b2', 'b3', 'b4'],
    'L': ['l1', 'l2', 'l3', 'l4'],
    'D': ['d1', 'd2', 'd3', 'd4']
}

# Position과 Orientation을 붙여서 각각 지정정
goalState = {
    'ULB0': ('u1', 'l1'),
    'ULB1': ('b2', 'l1'),
    'ULB2': ('u1', 'b2'),
    'URB0': ('u2', 'b1'),
    'URB1': ('r2', 'b1'),
    'URB2': ('u2', 'r2'),
    'ULF0': ('u3', 'f1'),
    'ULF1': ('l2', 'f1'),
    'ULF2': ('u3', 'l2'),
    'URF0': ('u4', 'r1'),
    'URF1': ('f2', 'r1'),
    'URF2': ('u4', 'f2'),
    'DLB0': ('d3', 'b4'),
    'DLB1': ('l3', 'b4'),
    'DLB2': ('d3', 'l3'),
    'DRB0': ('d4', 'r4'),
    'DRB1': ('b3', 'r4'),
    'DRB2': ('d4', 'b3'),
    'DLF0': ('d1', 'l4'),
    'DLF1': ('f3', 'l4'),
    'DLF2': ('d1', 'f3'),
    'DRF0': ('d2', 'f4'),
    'DRF1': ('r3', 'f4'),
    'DRF2': ('d2', 'r3')
}


# 현재 cubie 상태 get
def get_current_state(cube):
    return {
        'ULB0': (cube['U'][0], cube['L'][0]),
        'ULB1': (cube['B'][1], cube['L'][0]),
        'ULB2': (cube['U'][0], cube['B'][1]),
        'URB0': (cube['U'][1], cube['B'][0]),
        'URB1': (cube['R'][1], cube['B'][0]),
        'URB2': (cube['U'][1], cube['R'][1]),
        'ULF0': (cube['U'][2], cube['F'][0]),
        'ULF1': (cube['L'][1], cube['F'][0]),
        'ULF2': (cube['U'][2], cube['L'][1]),
        'URF0': (cube['U'][3], cube['R'][0]),
        'URF1': (cube['F'][1], cube['R'][0]),
        'URF2': (cube['U'][3], cube['F'][1]),
        'DLB0': (cube['D'][2], cube['B'][3]),
        'DLB1': (cube['L'][2], cube['B'][3]),
        'DLB2': (cube['D'][2], cube['L'][2]),
        'DRB0': (cube['D'][3], cube['R'][3]),
        'DRB1': (cube['B'][2], cube['R'][3]),
        'DRB2': (cube['D'][3], cube['B'][2]),
        'DLF0': (cube['D'][0], cube['L'][3]),
        'DLF1': (cube['F'][2], cube['L'][3]),
        'DLF2': (cube['D'][0], cube['F'][2]),
        'DRF0': (cube['D'][1], cube['F'][3]),
        'DRF1': (cube['R'][2], cube['F'][3]),
        'DRF2': (cube['D'][1], cube['R'][2])
    }


# breadth-first-search(너비우선탐색)
def bfs(cube, key):
    queue = deque([(cube, get_current_state(cube), 0)])
    visited = set()
    while queue:
        current_cube, current_state, move_count = queue.popleft()

        if current_state[key] == goalState[key]:
            return move_count

        for move in ["F", "B", "R", "L", "U", "D", "F'", "B'", "R'", "L'", "U'", "D'"]:
            new_cube = copy.deepcopy(current_cube)
            rotations = 3 if move.endswith("'") else 1
            for _ in range(rotations):
                rotate_move(new_cube, move)

            new_state = get_current_state(new_cube)
            state_tuple = tuple((k, v) for k, v in sorted(new_state.items()))

            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((new_cube, new_state, move_count + 1))

    return -1


# bfs를 이용한 최소 move 탐색
def minmove(cube, position_orientation):
    key = position_orientation[0] + str(position_orientation[1])
    return bfs(cube, key)


# summation 기반 휴리스틱 함수
def hSum(cube):
    total_sum = 0
    for cubei in ['ULB', 'URB', 'ULF', 'URF', 'DLB', 'DRB', 'DLF', 'DRF']:
        for i in range(3):
            min_move = minmove(cube, (cubei, i))

            total_sum += min_move
    return total_sum / 4


# maximum 기반 휴리스틱 함수수
def hMax(cube):
    max_moves = 0
    for corner in ['ULB', 'URB', 'ULF', 'URF', 'DLB', 'DRB', 'DLF', 'DRF']:
        for i in range(3):
            min_move = minmove(cube, (corner, i))
            if min_move > max_moves:
                max_moves = min_move
    return max_moves


# IDA* 재귀 탐색
def search(cube, g, threshold, goal, path, visited):
    f = g + hSum(cube)
    if f > threshold:
        return (f, None)
    if cube == goal:
        return (True, path)

    minimum = float('inf')
    min_path = None

    state_tuple = tuple(sorted((k, v) for k, v in get_current_state(cube).items()))

    if state_tuple in visited:
        return (float('inf'), None)  # 해당 경로는 탐색하지 않아도 됨
    visited.add(state_tuple)

    for successor, move in get_successors(cube):
        new_path = path[:]
        new_path.append(move)
        temp, suc_path = search(successor, g + 1, threshold, goal, new_path, visited)
        if temp == True:
            return (True, suc_path)
        if temp < minimum:
            minimum = temp
            min_path = suc_path

    return (minimum, min_path)


# IDA* 알고리즘(hSum)
def ida_star(cube_start, goal):
    threshold = hSum(cube_start)
    path = []
    visited = set()

    while True:
        temp, solution_path = search(cube_start, 0, threshold, goal, path, visited)
        if temp == True:
            return solution_path
        elif temp is None or temp == threshold:  # 개선점이 없거나 임계값 내에 경로를 찾을 수 없음
            return None
        threshold = temp


# 가능한 모든 이동 적용해 후계자 생성
def get_successors(node):
    from copy import deepcopy
    successors = []
    moves = ["F", "B", "R", "L", "U", "D", "F'", "B'", "R'", "L'", "U'", "D'"]
    for move in moves:
        new_cube = deepcopy(node)
        base_move = move.strip("'")
        rotations = 3 if move.endswith("'") else 1
        for _ in range(rotations):
            rotate_move(new_cube, base_move)
        successors.append((new_cube, move))
    return successors


# 섞인 큐브 상태 .JSON 저장
def save_cube_to_json(cube, filename='scrambled_cube.json'):
    with open(filename, 'w') as file:
        json.dump(cube, file, indent=4)
    print(f'Cube configuration saved to {filename}')


def main():
    print('INIT===============================================================')
    printCube(cube)
    print(cube)
    currentState = get_current_state(cube)
    print(currentState)

    parser = argparse.ArgumentParser(description='IDA* Algorithm Visualization')
    parser.add_argument('-n', type=int, default=5, help='Number of moves to scramble (default: 5)')

    args = parser.parse_args()

    scramble_str = ''
    moves = ["F", "B", "R", "L", "U", "D", "F'", "B'", "R'", "L'", "U'", "D'"]

    selected_moves = random.choices(moves, k=args.n)
    scramble_str = ' '.join(selected_moves)
    for move in scramble_str.split(' '):
        base_move = move.split("'")[0]
        rotations = 3 if move.endswith("'") else 1
        for _ in range(rotations):
            rotate_move(cube, base_move)

    print('\n===================================================================')
    print(f'MIXED --> {scramble_str}')
    print('===================================================================')

    print('\nMIXED==============================================================')
    printCube(cube)
    print(cube)

    save_cube_to_json(cube)

    solutions = ida_star(cube, goal=goalCube)
    if solutions:
        solution_moves = ' --> '.join(solutions)
        print('\n===================================================================')
        print(f'SOLUTIONS --> {solution_moves}')
        print('===================================================================\n')

        for move in solutions:
            base_move = move.strip("'")
            rotations = 3 if move.endswith("'") else 1
            for _ in range(rotations):
                rotate_move(cube, base_move)
            printCube(cube)
            print(f'Move: {move}')
            print('===================================================================\n')

    else:
        print('No solution found.')


if __name__ == '__main__':
    main()
