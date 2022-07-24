import random
# 0~2 숫자를 랜덤으로 뽑아내는 코드
computer = random.randint(0,2)
# 랜덤으로 나온 수를 가위 바위 보로 변환하는 함수
def rsp(a):
    if a == 0:
        return '가위'
    elif a == 1:
        return '바위'
    else :
        return '보'

my=input("가위=0 바위=1 보=2    ")
my=int(my)

# 승자를 정하는 함수, a=나 b=컴퓨터
def winner(a,b):
    if a-b==0:
        print("무승부!")
    elif a-b==1:
        print("나 승리!")
    elif a-b==-1:
        print("컴퓨터 승리!")
    elif a-b==2:
        print("컴퓨터 승리!")
    elif a-b==-2:
        print("나 승리!")

print("나:",rsp(my)) 
print("컴퓨터:",rsp(computer))
winner(my,computer)