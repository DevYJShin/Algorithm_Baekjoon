import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# 메모리 초과
# import sys
#
# n = int(sys.stdin.readline())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(sys.stdin.readline()))
#
# sorted_list = sorted(num_list)
#
# for i in sorted_list:
#     print(i)