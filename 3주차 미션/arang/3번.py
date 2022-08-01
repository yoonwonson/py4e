# 짝수, 중앙값
def find_even_number(n, m):
    for thing in numbers :
        if thing%2 == 0 :
            print(thing,'짝수')
    if ((n+m)/2)%2 == 0 :
        print('중앙값 :',int(((n+m)/2)))

# 입력
while True :
    try :
        n = int(input("첫 번째 수 입력 : "))
        break
    except :
        print('숫자를 입력해주세요')
        continue
while True :
    try :
        m = int(input("두 번째 수 입력 : "))
        if m<= n :
            (print('첫 번째 수보다 큰 숫자를 입력해주세요.'))
        else :
            break
    except :
        print('숫자를 입력해주세요')
        continue
numbers = [ i for i in range(n,m+1)]

# 출력
find_even_number(n,m)
