'''

문제 3: 우선순위 큐 구현

'''

import heapq

tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')]

heapq.heapify(tasks)
result = [i[1] for i in tasks]


print(result)
