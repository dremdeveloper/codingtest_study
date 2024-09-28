# 뒤의 기능이 앞의 기능보다 먼저 개발 될 수도 있다. 
# 이때, 뒤의 기능은 앞의 기능이 배포될 때 함께 배포되어야 한다. 
# 배포는 하루에 한 번만 할 수 있고, 하루의 끝에 이루어진다. 

from collections import deque

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))

progresses = deque(progresses)
result=[]
def solutions(progresses, speeds):
    end = len(speeds)
    cnt = 0
    total=0
    while 1:
        if total ==len(progresses):
            break
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        
        for i in range(len(progresses)):
            if i>=total:
                if progresses[i]>=100:
                    cnt+=1
                    total +=1
                else:
                    break
        if cnt>=1:
            result.append(cnt)
            cnt = 0

        if total == 5:
            break

solutions(progresses, speeds)
print(result)
