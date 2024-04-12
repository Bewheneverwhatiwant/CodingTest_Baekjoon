from itertools import combinations # 벽 3개를 세우는 조합 경우의 수를 위함
from collections import deque
import copy # 3개 벽을 뽑는 경우마다 map 복사하기 위함

# 각 조합(벽을 세우는 경우의 수)마다 virus_positions와 temp_map으로 bfs
def bfs(virus_start, lab_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque(virus_start)
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2 # 바이러스 확산 처리
                queue.append((nx, ny))



# 입력받기
n, m = map(int, input().split())
original_map = [] # 원래 지도

virus_positions = [] # 바이러스 감염지대
empty_positions = [] # 청정지대
max_safe_area = 0 # 최대 안전지대

for i in range(n):
    row = list(map(int, input().split()))
    original_map.append(row)
    
    for j in range(m):
        if row[j] == 2:
            virus_positions.append((i, j)) # 바이러스 위치 추가
        elif row[j] == 0:
            empty_positions.append((i, j))




# 안전지대 넓이 계산 메소드
def calculate_safe_area(lab_map):
    return sum(row.count(0) for row in lab_map) # 이건 제출 후 최적화한 부분..^^



# empty_positions에서 무작위로 3개를 뽑는(벽) 경우를 따지기 위해 collections를 사용해봄
# walls에는 3개의 위치 좌표(벽)가 들어가게 됨
for walls in combinations(empty_positions, 3):
    
    # 조합 경우의 수마다 map을 사용해야 하는데, 원래 map은 냅두고 계속 복사해서 써야하므로
    # copy.copy(얕은복사)가 아닌 copy.deepcopy(깊은복사)로 map을 복사한다
    # 얕은복사하면 원래 map이 변하면서 오류남
    temp_map = copy.deepcopy(original_map)
    
    for wx, wy in walls:
        temp_map[wx][wy] = 1 # walls에서 (wx, wy)가 벽으로 설정된다
    
    # 3개(벽) 조합 경우마다 바이러스 확산 시뮬레이션
    bfs(virus_positions, temp_map)
    
    # 안전지대 넓이 계산 메소드 사용
    safe_area = calculate_safe_area(temp_map)
    # max 안전지대 찾기
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
