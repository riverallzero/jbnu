import pygame
import sys
import math
import argparse
import random

# Grid World Size ===================
gridWorldWidth = 600
gridWorldHeight = 600

# PyGame ============================
pygame.init()
win = pygame.display.set_mode((gridWorldWidth, gridWorldHeight))
pygame.display.set_caption('A Star Algorithm')
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)

grid = []
openSet = []
closeSet = []
path = []


class Cell:
    def __init__(self, i, j):
        self.x, self.y = i, j  # 위치 정보
        self.f, self.g, self.h = 0, 0, 0  # f(n) = g(n) + h(n)
        self.neighbors = []  # 셀 이웃 목록
        self.prev = None  # 이전 셀 추적
        self.wall = False  # 벽 여부

    # 셀 채우기(시작점, 종료점, 벽)
    def show(self, win, col, startPoint, endPoint):
        if self.wall == True:
            col = (200, 200, 200)
        pygame.draw.rect(win, col, (self.x * gridW, self.y * gridH, gridW - 1, gridH - 1))

        if self == startPoint:
            text = font.render('S', True, (0, 0, 0))
            win.blit(text, (self.x * gridW + gridW // 4, self.y * gridH + gridH // 4))
        if self == endPoint:
            text = font.render('G', True, (0, 0, 0))
            win.blit(text, (self.x * gridW + gridW // 4, self.y * gridH + gridH // 4))

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])


def euclidean(a, b):
    return math.sqrt((a.x - b.x) ** 2 + abs(a.y - b.y) ** 2)


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def create_grid(M, N):
    global cols, rows, gridW, gridH, grid, startPoint, endPoint

    cols = gridWorldWidth // M
    rows = gridWorldHeight // N

    # 각 그리드 셀의 크기
    gridW = gridWorldWidth // cols
    gridH = gridWorldHeight // rows

    grid.clear()
    openSet.clear()  # 방문하지 않은 셀
    closeSet.clear()  # 방문한 셀
    path.clear()

    # 모든 격자 칸에 셀 객체 생성하고 이웃 추가
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(Cell(i, j))
        grid.append(arr)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].add_neighbors(grid)

    # 랜덤으로 벽 생성
    total_cells = cols * rows
    obstacles_count = int(total_cells * inc_obstacle_ratio)

    # 시작점과 종료점 고정 설정
    startPoint = grid[0][0]
    endPoint = grid[18][15]

    while obstacles_count > 0:
        i = random.randint(0, cols - 1)
        j = random.randint(0, rows - 1)
        if not grid[i][j].wall and grid[i][j] != startPoint and grid[i][j] != endPoint:
            grid[i][j].wall = True
            obstacles_count -= 1

    openSet.append(startPoint)


# 마우스로 벽 생성
def clickWall(pos, state):
    i = pos[0] // gridW
    j = pos[1] // gridH

    # 시작점 또는 종료점 셀을 클릭한 경우 클릭 무시
    if grid[i][j] == startPoint or grid[i][j] == endPoint:
        return
    grid[i][j].wall = not grid[i][j].wall


def close():
    pygame.quit()
    sys.exit()


def main(M, N, mode, inc_obstacle_ratio):
    global cols, rows, startPoint, endPoint, openSet, closeSet, path
    closeSet_count = 0

    create_grid(M, N)

    flag = False # 경로 발견 여부
    noFlag = True # 경로 찾지 못한 경우
    startFlag = False # 경로 탐색 시작 여부

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clickWall(pygame.mouse.get_pos(), True)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    clickWall(pygame.mouse.get_pos(), True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startFlag = True

        # A* Algorithm 실행
        if startFlag:
            if len(openSet) > 0:
                winner = 0
                for i in range(len(openSet)):
                    if openSet[i].f < openSet[winner].f:
                        winner = i

                current = openSet[winner]

                if current == endPoint:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev
                    if not flag:
                        flag = True
                        print('\nPATH EXIST!===========================')
                        print(f'total explored cell: {closeSet_count}')
                        print('======================================')
                    elif flag:
                        continue

                if flag == False:
                    openSet.remove(current)
                    closeSet.append(current)

                    closeSet_count += 1
                    for neighbor in current.neighbors:
                        if neighbor in closeSet or neighbor.wall:
                            continue
                        tempG = current.g + 1

                        newPath = False
                        if neighbor in openSet:
                            if tempG < neighbor.g:
                                neighbor.g = tempG
                                newPath = True
                        else:
                            neighbor.g = tempG
                            newPath = True
                            openSet.append(neighbor)

                        if newPath:
                            if mode == 'euclidean':
                                neighbor.h = euclidean(neighbor, endPoint)
                            elif mode == 'manhattan':
                                neighbor.h = manhattan(neighbor, endPoint)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.prev = current

            else:
                if noFlag:
                    print('\nPATH DOES NOT EXIST!==================')
                    print(f'total explored cell: {closeSet_count}')
                    print('======================================')
                    break

        win.fill((0, 20, 20))

        for i in range(cols):
            for j in range(rows):
                cell = grid[j][i]
                cell.show(win, (255, 255, 255), startPoint, endPoint)

                try:
                    if cell == endPoint:
                        cell.show(win, (255, 255, 255), startPoint, endPoint)
                except Exception:
                    pass

        # 찾은 경로 노란색으로 연결
        if flag and path:
            for i in range(len(path) - 1):
                if i == 0:  # 마지막 경로와 종료셀 연결
                    pygame.draw.line(win, (255, 255, 0),
                                     (path[i].x * gridW + gridW // 2, path[i].y * gridH + gridH // 2),
                                     (endPoint.x * gridW + gridW // 2, endPoint.y * gridH + gridH // 2), 5)
                start_pos = (path[i].x * gridW + gridW // 2, path[i].y * gridH + gridH // 2)
                end_pos = (path[i + 1].x * gridW + gridW // 2, path[i + 1].y * gridH + gridH // 2)
                pygame.draw.line(win, (255, 255, 0), start_pos, end_pos, 5)

        pygame.display.flip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A* Algorithm Visualization')
    parser.add_argument('-m', type=int, default=30, help='Number of columns (default: 30)')
    parser.add_argument('-n', type=int, default=30, help='Number of rows (default: 30)')
    parser.add_argument('-inc_obstacle_ratio', type=float, default=0.2,
                        help='Obstacle density as a percentage of the grid (default: 0.2)')
    parser.add_argument('-mode', type=str, default='euclidean', choices=['euclidean', 'manhattan'],
                        help='Mode for distance calculation euclidean vs manhattan (default: euclidean)')

    args = parser.parse_args()

    M = args.m
    N = args.n
    mode = args.mode
    inc_obstacle_ratio = args.inc_obstacle_ratio

    main(M, N, mode, inc_obstacle_ratio)
