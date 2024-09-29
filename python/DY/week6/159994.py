# 카드 뭉치

cards1 = list(input().split())
cards2 = list(input().split())
goal = list(input().split())

# 규칙을 따라 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 
# 만들 수 있는지 알고싶음

'''
1. 원하는 카드 문치에서 카드를 순서대로 한 장씩 사용
2. 한 번 사용한 카드는 다시 사용할 수 없음
3. 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음
4. 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없음

'''

def solutions(cards1, cards2, goal):

    one=0
    two=0
    check = 0
    for i in goal:
        if cards1 and (one<=len(cards1)-1) and cards1[one] == i:
            one+=1
        elif cards2 and (two<=len(cards2)-1) and cards2[two] == i:
            two+=1
            
        else:
            print("No")
            check = 1
            break

    if check ==0:
        print("Yes")

solutions(cards1, cards2, goal)
