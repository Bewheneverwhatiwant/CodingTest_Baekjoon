from collections import deque

def bfs(maze, N, M):
    # BFS의 기본: 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    #탐색 시작
    while queue:
        x, y = queue.popleft()
        
        #현재 위치 x, y에서 dx, dy를 더해 4가지 방향으로의 위치 확인
        #확인하는 위치가 nx, ny
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로 범위를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            #이동할 수 없는 칸인 경우 무시
            if maze[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            #nx, ny가 1인 경우 1씩 누적
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
                
    #도착 지점까지의 최단 거리 리턴
    return maze[N-1][M-1]


#파이썬으로 입력받기
#프로그래머스 때문에 까먹을뻔
N, M = map(int, input().split())

#미로 만들어서 주기
maze = [ list(map(int, list(input()))) for _ in range(N) ]

print(bfs(maze, N, M))
