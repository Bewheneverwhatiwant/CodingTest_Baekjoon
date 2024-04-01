n = int(input())
l = int(input())

# 노드들이 1부터 시작하므로 0번은 비워두고 n+1번까지로 해서 빈 2차원 배열
graph = [ [] for _ in range(n+1) ]

# 입력받은 값과 연결된 노드들을 append로 추가
# 1번 노드 - 2 - 5 연결이므로 graph[1] = [2, 5]

for _ in range(l):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 0번 인덱스를 비워두므로
visited = [0] * (n+1)

# 현재 노드 v에 방문(=바이러스 감염) 했으면 1로 바꾸고
# 해당 노드의 연결된 노드들 중에서 하나씩 살펴봄
# 만약 0이면, 아직 방문 x -> dfs 재귀 호출

def dfs(graph, v, visited):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited)-1) # 1번 노드의 방문은 제외하는 것