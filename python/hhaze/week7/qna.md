##  질문

1. 큐를 이용하여 주어진 데이터를 순차적으로 처리하는 알고리즘을 설계하고 구현하세요. 이 알고리즘의 시간 복잡도는 어떻게 되나요? 큐를 사용하지 않고도 데이터를 순차적으로 처리할 수 있는 다른 방법을 설명하세요.

- 큐를 이용하여 주어진 데이터를 순차적으로 처리하는 알고리즘
    ```python
    from collections import deque

    def solution(data):
        queue = deque(data)
        result = []

        while queue:
            item = queue.popleft()
            # 원하는 처리
            result.append(item)
        
        return result
    ```
    - 시간 복잡도는 O(N)
- 큐를 사용하지 않고 데이터를 처리할 수 있는 다른 방법
    ```python
    def solution(data):
        result = list(map(lambda x: # 원하는 처리 hjj))
        return result
    ```

2. 주어진 문자열에서 연속된 중복된 문자를 제거한 새로운 문자열을 반환하는 알고리즘을 설계하고 구현하세요. 단, 문자열 내에서 문자의 순서는 유지해야 합니다. 시간 복잡도를 분석하세요.
```python
from collections import deque

def solution(s):
    queue = deque()
    queue.append(s[0])

    for i in range(1, len(s)):
        if s[i] != queue[len(queue) - 1]:
            queue.append(s[i])
    
    return ''.join(queue)
```
- 시간 복잡도는 O(N)

3. 큐와 스택의 차이점을 설명하고, 각각의 자료구조가 적합한 상황을 예시와 함께 설명해보세요. 두 자료구조의 시간 복잡도에 대한 일반적인 차이도 설명하세요.
- 큐
    - FIFO
    - 줄을 선 순서대로 처리할 때 (작업 대기열, 이벤트 처리 등)
- 스택
    - LIFO
    - 함수 호출 관리, 괄호 매치 등
- 큐와 스택 모두 삽입과 삭제 연산에 대한 시간 복잡도는 O(1)

4. 큐를 이용하여 우선순위가 있는 작업을 처리하는 방법에 대해 설명하세요. 우선순위가 높은 작업을 먼저 처리할 수 있는 자료구조의 동작 원리와 그에 따른 시간 복잡도를 설명해보세요.
- 우선순위 큐(최대 힙 트리 구조)를 사용
    - 우선순위 큐는 각 원소에 우선순위가 지정되어 있고, 우선순위가 높은 원소가 먼저 처리되는 자료구조
- 삽입 시 새 원소를 힙의 마지막에 추가한 후 부모 노드와 비교하며 필요할 때 위치 교환 -> 시간 복잡도는 O(log N)
- 삭제 시 루트 노드를 제거하고 힙의 마지막 원소를 루트로 이동시킨 후 자식 노드와 비교하며 필요할 때 위치 교환 -> 시간 복잡도는 O(log N)
- 조회 시 루트 노드의 값을 반환 -> 시간 복잡도는 O(1)

---

## 실전 문제

### 문제 1: BFS(너비 우선 탐색) 알고리즘 구현

주어진 그래프에서 시작 노드부터 목표 노드까지의 최단 경로를 찾는 BFS 알고리즘을 큐를 이용하여 구현하세요.

- **입력**: 그래프와 시작 노드, 목표 노드가 주어집니다.
- **출력**: 시작 노드부터 목표 노드까지의 최단 경로를 리스트로 출력합니다.

#### 예시 입력/출력

```python
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

# 예시 출력 1
['A', 'C', 'F']
```

#### 입출력 설명

- 예시 1에서는 'A'에서 'F'까지 가는 최단 경로는 ['A', 'C', 'F']입니다.

```python
from collections import deque

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
```

### 문제 2: 캐시 구현

주어진 요청을 처리하는 간단한 캐시 시스템을 큐를 이용하여 구현하세요. 캐시는 고정된 크기를 가지며, 새로운 데이터가 들어올 때 공간이 부족하면 가장 오래된 데이터를 제거합니다.

- **입력**: 캐시 크기와 요청 리스트가 주어집니다.
- **출력**: 각 요청이 처리될 때마다 캐시의 상태를 출력합니다.

#### 예시 입력/출력

```python
# 예시 입력 1
cache_size = 3
requests = [1, 2, 3, 4, 1, 2, 5]

# 예시 출력 1
[1]
[1, 2]
[1, 2, 3]
[2, 3, 4]
[3, 4, 1]
[4, 1, 2]
[1, 2, 5]
```

#### 입출력 설명

- 예시 1에서는 캐시 크기가 3이므로, 공간이 부족하면 가장 오래된 요청을 제거하고 새로운 요청을 처리합니다.

```python
def solution(cache_size, requests):
    cache = deque()

    for request in requests:
        cache.append(request)
        
        if len(cache) > cache_size:
            cache.popleft()
        
        print(cache)
```

### 문제 3: 우선순위 큐 구현

우선순위가 부여된 작업을 처리하는 우선순위 큐를 구현하세요. 우선순위가 높은 작업이 먼저 처리되며, 같은 우선순위를 가진 작업들은 먼저 들어온 순서대로 처리됩니다.

- **입력**: 작업 목록과 각 작업의 우선순위가 주어집니다.
- **출력**: 우선순위에 따라 작업을 처리한 순서대로 출력합니다.

#### 예시 입력/출력

```python
# 예시 입력 1
tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')]

# 예시 출력 1
['Task B', 'Task D', 'Task C', 'Task A']
```

#### 입출력 설명

- 예시 1에서는 우선순위가 1인 'Task B'와 'Task D'가 먼저 처리되며, 같은 우선순위 내에서는 먼저 입력된 'Task B'가 먼저 처리됩니다.

```python
import heapq

def solution(tasks):
    queue = []
    result = []

    for priority, task in tasks:
        heapq.heappush(queue, (priority, task))
    
    while queue:
        result.append(heapq.heappop(queue)[1])
    
    return result
```

### 문제 4: 최대 슬라이딩 윈도우

주어진 배열에서 슬라이딩 윈도우 방식으로 최대 값을 구하는 문제입니다. 윈도우의 크기 k가 주어졌을 때, 배열에서 k개의 연속된 숫자 중 가장 큰 숫자를 찾으세요. 

- **입력**: 배열과 윈도우 크기 k가 주어집니다.
- **출력**: 각 윈도우에서의 최대 값을 리스트로 출력합니다.

#### 예시 입력/출력

```python
# 예시 입력 1
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# 예시 출력 1
[3, 3, 5, 5, 6, 7]
```

#### 입출력 설명

- 예시 1에서는 윈도우 크기가 3일 때, 각 슬라이딩 윈도우에서의 최대 값은 [3, 3, 5, 5, 6, 7]입니다.

```python
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
```