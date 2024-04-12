from collections import deque

def bfs(start, grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque([start])
    visited = [[False] * N for _ in range(N)]
    
    shark_size = 2
    shark_eat = 0
    time_spent = 0
    visited[start[0]][start[1]] = True

    while queue:
        # 거리가 최소인 물고기를 먼저 먹기 위해, dist를 기준으로 queue를 정렬
        # dist가 같다면 가장 위에 있는 물고기(x가 가장 작은 값) 선택
        # dist와 x가 같다면 가장 왼쪽에 있는 물고기(y가 가장 작은 값) 선택
        # sorted로 정렬하는데, 정렬기준은 x[2] > x[0] > x[1]가 된다.
        queue = deque(sorted(queue, key=lambda x: (x[2], x[0], x[1])))
        x, y, dist = queue.popleft()

        # 먹을 수 있는 물고기가 있으면
        if 0 < grid[x][y] < shark_size:
            grid[x][y] = 0  # 물고기 먹기
            shark_eat += 1
            
            if shark_eat == shark_size:  # 성장 조건
                shark_size += 1
                shark_eat = 0
                
            time_spent += dist  # 시간 증가
            queue = deque()  # 큐 초기화
            visited = [[False] * N for _ in range(N)]  # 방문 초기화
            queue.append((x, y, 0))  # 새 위치에서 다시 시작
            visited[x][y] = True
            continue

        # 다음 위치 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] <= shark_size:  # 이동 가능 조건
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return time_spent

def solve():
    N = int(input())
    grid = []
    start = (0, 0, 0)  # 시작 위치 (x, y, 거리(dist))
    
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        
        for j in range(N):
            if row[j] == 9:
                start = (i, j, 0)
                
                grid[i][j] = 0  # 시작 위치를 빈 칸으로 설정

    print(bfs(start, grid, N))

solve()
