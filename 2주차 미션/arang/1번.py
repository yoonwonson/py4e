import random
computer = random.randint(0,2)
def com() :
    if computer == 0 :
        return '가위'
    elif computer == 1 :
        return '바위'
    elif computer == 2 :
        return '보'
my = input('가위 바위 보')
def rsp(my) :
    if my=='가위' :
        if computer==0 :
            return '무승부!'
        elif computer==1 :
            return '컴퓨터 승리!'
        elif computer==2 :
            return '내가 이겼다!'
    if my=='바위' :
        if computer==0 :
            return '내가 이겼다!'
        elif computer==1 :
            return '무승부!'
        elif computer==2 :
            return '컴퓨터 승리!'
    if my=='보' :
        if computer==0 :
            return '컴퓨터 승리!'
        elif computer==1 :
            return '내가 이겼다!'
        elif computer==2 :
            return '무승부!'
print('나:',my)
print('컴퓨터:',com())
print(rsp(my))
