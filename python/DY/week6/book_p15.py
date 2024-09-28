from collections import deque

queue = deque()

n, k = map(int, input().split()) 
# 사람이 n 까지의 번호표를 가짐
# 임의의 숫자 k 

tmp = [i for i in range(1, n+1)]
queue = deque(tmp)
# print(queue)

# 1번 사람 기준으로 k 번째 사람 삭제
# k 번째 사람 다음 사람 기준으로 다시 k 번째 사람 삭제 

# 마지막에 살아남는 사람 번호 return 

def solutions(n, k, queue):
    cnt = 1
    while 1:
        if cnt == k:
            if len(queue)==1:
                value = queue.popleft()
                return value
            else:
                value = queue.popleft()
                #print(queue)
                cnt=0
        else:
            value = queue.popleft()
            queue.append(value)
            cnt+=1

print(solutions(n, k, queue))

