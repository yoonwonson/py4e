
# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
numbers = [ i for i in range(n,m+1)]

# 짝수, 중앙값
def find_even_number(n, m):
    for thing in numbers :
        if thing%2 == 0 :
            print(thing,'짝수')
    if ((n+m)/2)%2 == 0 :
        print('중앙값 :',int(((n+m)/2)))
# 출력
find_even_number(n,m)
