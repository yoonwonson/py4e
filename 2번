# 입력
def rsp(a):
    if a == '가위' or '0':
        return 0
    elif a == '바위' or '1':
        return 1
    else :
        return 2

import random
computer = random.choice(['가위','바위','보'])

while True :
    try :
        games = int(input("몇 판을 진행하시겠습니까? : "))
    except :
        print('숫자를 입력해주세요.')
        continue
    try :
        user = input("가위:0,바위:1,보:2를 입력하세요.")
        if user == '가위' or '바위' or '보' or '1' or '2' or '0' :
            break
    except :
        print("가위:0,바위:1,보:2 중에서 입력해주세요.")
        continue

#가위바위보
def rsp_advanced(games) :

    zork = 0
    while True :
        if games>0 :
            zork = zork + 1
            games = games - 1
            minus = int(rsp(user)) - int(rsp(computer))
            if minus == 1 or -2 :
                print('====================================')
                print('나 :',user)
                print('컴퓨터 :',computer)
                print(zork,"번째 판 내가 이겼다!")
                print('====================================')
                continue
            elif minus == 0 :
                print('====================================')
                print('나 :',user)
                print('컴퓨터 :',computer)
                print(zork,"번째 판 비겼다!")
                print('====================================')
                continue
            else :
                print('====================================')
                print('나 :',user)
                print('컴퓨터 :',computer)
                print(zork,"번째 판 졌다!")
                print('====================================')
                continue
        else :
            break

(rsp_advanced(games))
