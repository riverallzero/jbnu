import sys

def canGo(curr_locs, visited):
    c, r = curr_locs

    if c < N and r < N:
        if visited[c][r]:
            return 'Hing'
        
        visited[c][r] = True

        start_val = game_map[c][r]
        moves = [(c, r + start_val), (c + start_val, r)]  # 오른쪽 이동, 아래쪽 이동

        for move in moves:
            if move[0] == N - 1 and move[1] == N - 1:
                return 'HaruHaru'
            
            elif move[0] < N and move[1] < N:
                result = canGo(move, visited)
                if result == 'HaruHaru':
                    return 'HaruHaru'
    return 'Hing'

if __name__ == '__main__':
    lines = list(sys.stdin.readlines())

    N = int(lines[0].strip())
    game_map = [list(map(int, line.strip().split())) for line in lines[1:]]

    visited = [[False for _ in range(N)] for _ in range(N)]
    
    print(canGo((0, 0), visited))