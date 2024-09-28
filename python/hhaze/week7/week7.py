from collections import deque

# 2
def solution(s):
    queue = deque()
    queue.append(s[0])

    for i in range(1, len(s)):
        if s[i] != queue[len(queue) - 1]:
            queue.append(s[i])
    
    return ''.join(queue)

print(solution("aabbccaa"))

# 문제 1: BFS(너비 우선 탐색) 알고리즘 구현
def solution(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        (node, path) = queue.popleft()

        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path            

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return None 

print(solution({'A' : ['B', 'C'], 'B' : ['A', 'D', 'E'], 'C' : ['A', 'F'], 'D' : ['B'], 'E' : ['B', 'F'], 'F' : ['C', 'E']}, 'A', 'F'))

# 문제 2: 캐시 구현
def solution(cache_size, requests):
    cache = deque()

    for request in requests:
        cache.append(request)
        
        if len(cache) > cache_size:
            cache.popleft()
        
        print(cache)

print(solution(3, [1, 2, 3, 4, 1, 2, 5]))

# 문제 3: 우선순위 큐 구현
import heapq

def solution(tasks):
    queue = []
    result = []

    for priority, task in tasks:
        heapq.heappush(queue, (priority, task))
    
    while queue:
        result.append(heapq.heappop(queue)[1])
    
    return result

print(solution([(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')]))

# 문제 4: 최대 슬라이딩 윈도우
def solution(arr, k):
    cache = deque()
    result = []

    for i in arr:
        cache.append(i)
        
        if len(cache) > k:
            cache.popleft()

        if len(cache) == k:
            result.append(max(cache))
        
    return result

print(solution([1, 3, -1, -3, 5, 3, 6, 7], 3))