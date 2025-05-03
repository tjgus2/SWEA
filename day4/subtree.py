# 트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.

def dfs(node):
    count = 1
    for child in tree[node]:
        count += dfs(child)
    return count

t = int(input())

for test_case in range(1, t+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]
    for i in range(0, len(data), 2):
        parent, child = data[i],data[i+1]
        tree[parent].append(child)

    
    print("#"+str(test_case), dfs(N))