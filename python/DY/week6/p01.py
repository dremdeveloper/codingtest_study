'''

실전 문제
문제 1: BFS(너비 우선 탐색) 알고리즘 구현

'''

from collections import deque


# 예시 입력 1
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}
start = 'A'
goal = 'F'

def sol(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()

        # node 인접노드 순회
        for i in graph[node]:
            if i == goal:
                return path + [i]
            elif i not in path:
                queue.append([i, path + [i]])

print(sol(graph, start, goal))



