from collections import deque

def bfs(N, K):
    # 둘 다 10만 이하
    max = 100000
    
    visited = [False] * (max + 1)
    queue = deque([N])
    visited[N] = True # 시작 위치 방문 처리
    time = 0
    
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            
            # 걷거나(+1 or -1) 순간이동(*2)하는 경우
            for next in (current - 1, current + 1, current * 2):
                # 범위를 벗어나지 않고 방문 안했으면
                if 0 <= next <= max and not visited[next]:
                    # 방문 처리
                    visited[next] = True
                    # 다음 위치를 큐에 추가
                    queue.append(next)
            
            # 동생에게 도착했다면 시간 반환
            if current == K:
                return time
        
        # 1초 증가
        time += 1

N, K = map(int, input().split())

print(bfs(N, K))