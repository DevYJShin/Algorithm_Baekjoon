T = int(input())                # 요리 시간 T를 int type으로 입력을 받는다.

button = [300, 60 ,10]          # 버튼 300, 60, 10을 리스트에 담아준다.

if T % 10 != 0:                 # 만약 T를 10으로 나누었을 때 나머지가 0이 아니면 -1 출력
    print(-1)
else:                           # 그게 아니라면
    for i in button:            # button 안에 있는 i 요소 반복
        print(T//i, end = " ")  # T를 i로 나누었을 때 몫을 띄어쓰기로 출력
        T = T % i               # T는 T를 i로 나누었을 때 몫으로 바꾼다.