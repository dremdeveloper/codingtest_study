# 문제 1
def solution(s):
    dic = { "홍길동": 85, "이순신": 90, "장영실": 78 }

    return dic[s]

print(solution('홍길동'))

# 문제 2
def solution(dic, value):
    result = {}

    for k, v in dic.items():
        if v > value:
            result[k] = v
    
    return result

print(solution({ "a": 10, "b": 20, "c": 5 }, 10))

# 문제 3
def solution(dic1, dic2):
    result = dic1

    for k, v in dic2.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v

    return result

print(solution({ "a": 1, "b": 2 }, { "b": 3, "c": 4 }))

# 문제 4
def solution(arr):
    result = {}

    for i in arr:
        result[i] = len(i)
    
    return result

print(solution(["apple", "banana", "pear"]))

# 문제 5
def solution(dic):
    value_sum = sum(dic.values())
    value_len = len(dic)
    result = round(value_sum / value_len, 2)

    return result

print(solution({ "홍길동": 85, "이순신": 90, "장영실": 78 }))