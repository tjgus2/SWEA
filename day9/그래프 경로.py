# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

def dfs(graph, visited, current, goal):
    # 현재 노드를 방문 처리
    visited[current] = True

    # 도착 노드에 도달했으면 True 반환
    if current == goal:
        return True

    # 인접한 노드들에 대해 탐색
    for neighbor in graph[current]:
        if not visited[neighbor]:
            if dfs(graph, visited, neighbor, goal):
                return True

    return False


T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 노드 수, 간선 수

    # 인접 리스트 방식으로 그래프 초기화
    graph = [[] for _ in range(V + 1)]

    # 간선 정보 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)  # 방향성 그래프이므로 start -> end만 추가

    # 출발점 S, 도착점 G 입력
    S, G = map(int, input().split())

    visited = [False] * (V + 1)

    # DFS 수행
    result = 1 if dfs(graph, visited, S, G) else 0

    # 결과 출력
    print(f"#{test_case} {result}")
