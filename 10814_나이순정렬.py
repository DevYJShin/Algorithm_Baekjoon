v = [input().split() for _ in range(int(input()))] # 입력
for i in v : i[0] = int(i[0])
v.sort(key=lambda x:x[0]) # sorting
for i in v : print(" ".join(map(str, i))) # 출력