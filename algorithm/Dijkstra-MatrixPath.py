import sys
import heapq

def minTime(N, M, game_map):
    distance_M = [[float('inf')] * M for _ in range(N)]
    distance_M[0][0] = game_map[0][0]
    
    priority_que = [(game_map[0][0], 0, 0)]
    
    moves = [(0, 1), (1, 0)]
    
    while priority_que:
        current_time, row, col = heapq.heappop(priority_que)
        
        if row == N-1 and col == M-1:
            return current_time
        
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            
            if 0 <= new_row < N and 0 <= new_col < M:
                new_time = current_time + game_map[new_row][new_col]
                
                if new_time < distance_M[new_row][new_col]:
                    distance_M[new_row][new_col] = new_time
                    heapq.heappush(priority_que, (new_time, new_row, new_col))
    
if __name__ == '__main__':
    # answers = 40
    # inputs = [
    #     '4 4\n',
    #     '6 7 12 5\n',
    #     '5 3 11 18\n',
    #     '7 17 3 3\n',
    #     '8 10 14 9'  
    # ]

    inputs = sys.stdin.readlines()

    N, M = map(int, inputs[0].split())
    game_map = [list(map(int, line.strip().split())) for line in inputs[1:]]

    print(minTime(N, M, game_map))