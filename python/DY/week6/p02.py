'''

문제 2: 캐시 구현




'''

from collections import deque


cache_size = 3
requests = [1, 2, 3, 4, 1, 2, 5]

queue=deque()

for i in requests:
    if not queue or len(queue)<cache_size:
        queue.append(i)
    elif len(queue) == cache_size:
        queue.popleft()
        queue.append(i)
    
    print(list(queue))
