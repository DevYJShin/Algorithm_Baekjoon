from sys import stdin                      # readline을 사용하기 위해 import
from math import factorial                 # factorial을 사용하기 위해 import

while True:                                # 0을 입력할 때까지 반복
    number = stdin.readline().rstrip()     # 팩토리얼 진법 숫자 입력  

    number_len = len(number)               # 입력한 팩토리얼 진법 숫자의 길이를 저장하는 변수 선언

    decimal_number = 0                     # 팩토리얼 진법 숫자를 10진법으로 읽은 값을 저장할 변수 선언

    if number == '0':                      # 입력한 팩토리얼 진법 숫자가 0이라면
        break                              # 반복문 탈출

    for i in range(number_len):            # 팩토리얼 진법 숫자의 길이만큼 반복
        decimal_number += int(number[i]) * factorial(number_len -i)
                                           # 팩토리얼 진법 숫자에서 i번 자리의 값을 10진법으로 계산해
                                           # decimal_number에 더한다.

    print(decimal_number)                  # 팩토리얼 진법 숫자를 10진법 숫자로 읽은 값을 출력