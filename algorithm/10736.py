import sys


def minTime(N, game_map):
    sum_map = [[0] * N for _ in range(N)]

    sum_map[0][0] = game_map[0][0]

    for i in range(1, N):
        sum_map[i][0] = sum_map[i - 1][0] + game_map[i][0]
        sum_map[0][i] = sum_map[0][i - 1] + game_map[0][i]

    for i in range(1, N):
        for j in range(1, N):
            sum_map[i][j] = min(sum_map[i][j-1], sum_map[i-1][j]) + game_map[i][j]

    return sum_map[N-1][N-1]

if __name__ == '__main__':
    lines = list(sys.stdin.readlines())

    N = int(lines[0].strip().split()[0])
    game_map = [list(map(int, line.strip().split())) for line in lines[1:]]

    print(minTime(N, game_map))
