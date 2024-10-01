
# 목차

1. [질문](#질문)
2. [실전 문제](#실전-문제)

---

##  질문

1. **큐를 이용하여 주어진 데이터를 순차적으로 처리하는 알고리즘을 설계하고 구현하세요.
   이 알고리즘의 시간 복잡도는 어떻게 되나요? 큐를 사용하지 않고도 데이터를 순차적으로 처리할 수 있는 다른 방법을 설명하세요.**
   ```python 
   from collections import deque

   def sol (data) :
   queue = deque()

       for d in data:
          queue.append(d)

      while queue:
           current_d = queue.popleft()
         print(f"{current_d}")

   data = ['a','b','c','d','e']
   sol(data)
   ```
   - 시간복잡도 :
     - 입력 리스트의 모든 요소를 큐에 추가 : O(n)
     - 꺼낸 데이터에 대해서 print 출력 : O(n)<br>
     - 그러나 꺼낸 데이터에 대해서 print 처럼 간단한 작업이 아닌 더 복잡한 작업을 수행할 경우 (ex) 이중반복문 실행 ) : 시간 복잡도는 더 늘어날 수 있다.
   <br>
   - 다른 방법 : 
     - 리스트 사용
     - ```python
       def sol(data):
        list_data = []

        for d in data:
        list_data.append(d)

        while list_data:
        current_d = list_data.pop(0)
        print(f"{current_d}")

        data = ['a', 'b', 'c', 'd', 'e']
        sol(data)
     print 외의 다른 함수들을 호출하여 다양한 작업을 수행할 수 있다.
   

**2. 주어진 문자열에서 연속된 중복된 문자를 제거한 새로운 문자열을 반환하는 알고리즘을 설계하고 구현하세요.
   단, 문자열 내에서 문자의 순서는 유지해야 합니다. 시간 복잡도를 분석하세요.**
   ```python
   def sol(input):
    answer =""
    for i in input : 
        if(i not in answer) :
            answer += i 
    print(answer)
    return answer
```

**3. 큐와 스택의 차이점을 설명하고, 각각의 자료구조가 적합한 상황을 예시와 함께 설명해보세요. 두 자료구조의 시간 복잡도에 대한 일반적인 차이도 설명하세요.**
   - 큐 : 먼저 들어간 것이 먼저 처리되는 선입선출 구조를 가지고 있습니다.
     - 예시) 이메일 서버에서 들어오는 이메일을 큐에 저장하고, 서버가 차례대로 처리하여 사용자에게 전달합니다.
   - 스택 : 마지막에 들어온 것이 먼저 처리되는 후입선출 구조를 가지고 있습니다.  
     - 예시) 사용자가 웹페이지를 탐색할 때 마지막에 방문한 페이지가 가장 먼저 뒤로 가기 되므로, 스택 구조가 적합합니다.
   
   두 자료구조의 시간복잡도는 O(1), 모든 요소를 순회해야 할 때는 O(n)으로 동일합니다. 

**4. 큐를 이용하여 우선순위가 있는 작업을 처리하는 방법에 대해 설명하세요. 우선순위가 높은 작업을 먼저 처리할 수 있는 자료구조의 동작 원리와 그에 따른 시간 복잡도를 설명해보세요.**
    
우선순위 큐를 이용하여 처리한다. 삽입시 요소는 자신의 우선순위에 따라 적절한 위치에 배치되며, 우선순위가 동일한 요소는 FIFO 규칙에 따라 처리된다.
    가장 높은 우선순위를 가진 요소를 조회할 때는 O(1)로 루트 노드에 접근하여 값을 확인할 수 있다. 하지만 특정 우선순위를 가진 요소를 찾으려면 O(n)의 시간복잡도가 필요하다. 하지만 일반적으로 우선순위 큐는 특정 요소를 찾기보다는 우선순위에 따라 빠르게 삽입 및 삭제하는 데 초점을 맞춘다.
- 힙 : 우선순위 큐는 보통 최소 힙 또는 최대 힙을 사용하여 구현한다. 최소 힙에서는 루트 노드에 가장 작은 값이 위치하며, 이를 통해 빠르게 제거할 수 있다.
- 삽입 : 요소를 추가하고 우선순위를 고려한 뒤 위치를 재정렬 한다.
- 정렬 : 일반적으로 O(n log n) 또는 O(n^2)의 시간 복잡도가 필요하다.

    


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

#### solution
```python
from collections import deque

def sol(graph, start_node, goal_node):
    # 경로 리스트로 감싸기
    search_queue = deque([[start_node]])
    # 방문 노드 추적
    visited = set()
    
    while search_queue:
        current_path = search_queue.popleft()
        current = current_path[-1]
        
        if current == goal_node:
            return current_path
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                new_path = list(current_path)  
                new_path.append(neighbor)  
                search_queue.append(new_path) 
    
    return None
```

#### 입출력 설명

- 예시 1에서는 'A'에서 'F'까지 가는 최단 경로는 ['A', 'C', 'F']입니다.

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

#### solution
```python
def sol(size, requests) : 
    cache = deque(maxlen=size)
    
    for request in requests : 
        if request in cache :
            cache.remove(request)
            cache.append(request)
        else : 
            cache.append(request)
        print (list(cache))
    
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

#### solution
```python
import heapq

def sol(task_list):
    heap = []
    
    for priority, task in task_list:
        heapq.heappush(heap, (priority, task))

    result = []

    while heap:
        result.append(heapq.heappop(heap)[1])  # 작업만 반환
    
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


#### solution
```python
from collections import deque;
#index+k까지 검사
#deque() : 가장 앞의 숫자 pop
#가장 큰 숫자 max에 저장 
#answer list 에 저장 

def sol(arr, k) :
    answer = []
    for i in range(len(arr)-k+1):
        answer.append((max(arr[i:i+k])))
    return answer
    
```

deque를 이용한 방식 
```python
from collections import deque

def sol(arr, k):
    dq = deque()  # 최대값 후보들
    answer = []

    for i in range(len(arr)):
        # 덱의 첫 번째 인덱스가 현재 윈도우 범위를 벗어났으면 제거
        if dq and dq[0] <(i - k + 1): #현재 슬라이딩 윈도우의 시작 인덱스 보다 작은 경우
            dq.popleft()

        # 덱의 마지막 값이 현재 arr[i]보다 작으면 제거
        # 현재 인덱스 i의 값보다 작은 인덱스들을 반복 제거하여 최대값 후보를 유지
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

            # 현재 인덱스를 덱에 추가
        dq.append(i)

        if i >= k - 1:
            answer.append(arr[dq[0]])  # 덱의 첫 번째 값이 현재 윈도우의 최대값
            #같은 숫자가 반복되는 경우를 제외하면, 덱의 크기는 보통 1

    print(answer)
    return answer

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sol(arr, k))  # 출력: [3, 3, 5, 5, 6, 7]

```