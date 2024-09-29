'''

문제 4: 최대 슬라이딩 윈도우

'''

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

front = 0
rear = front+k

result = []

for i in range(len(arr)-k+1):
    if i != 0:
        front+=1

    result.append(max(arr[front: rear]))
    rear = front+k+1

print(result)