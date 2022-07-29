import random

def calcRsp(rsp, computer) :
    global userCnt
    global noneCnt
    global comCnt
    rspTable = {"0":0, "1":1, "2":2, "가위":0, "바위":1, "보":2}
    rspKeys = list(rspTable.keys())
    rspValue = list(rspTable.values())
    value = 0
    result = ""
    com = ""
    user = ""

    for idx, x in enumerate(rspKeys) :
        if x == rsp:
            value = int(rspTable[x])
            minus = value - computer
            if (minus == 1 or minus == -2) :
                result = "사용자 승리!"
                userCnt = userCnt + 1
            elif (minus == 0) :
                result = "비김!"
                noneCnt = noneCnt + 1
            else :
                result = "컴퓨터 승리!"
                comCnt = comCnt + 1
        if rspValue[idx] == computer :
            com = rspKeys[idx]
        if rspValue[idx] == value :
            user = rspKeys[idx]
    print()
    print("※※※※가위바위보※※※※")
    print("▶사용자 :", user)
    print("▶컴퓨터 :", com)
    print("▶결  과 :", result)
    print("※※※※※※※※※※※※")
    print()

def playGame(games) :
    for i in range(games) :
        while (1) :
            print("※※※※※※※",i+1,"번째 ※※※※※※※")
            rsp = str(input("가위/바위/보를 입력하세요.(가위:0, 바위:1, 보:2) => "))

            if (rsp == "0" or rsp == "1" or rsp == "2" or rsp == "가위" or rsp == "바위" or rsp == "보") :
                computer = random.randint(0, 2)
                calcRsp(rsp, computer)
                break
            else :
                print()
                print("※※※※※※※입력오류※※※※※※※")
                print("잘못 입력하셨습니다.(입력값 => "+rsp+")")
                print("※※※※※※※※※※※※※※※※※※")
                print()

    print()
    print("※※※※ 총 결과 ※※※※")
    print("▶사용자 : 승", userCnt, "무", noneCnt, "패", comCnt)
    print("▶컴퓨터 : 승", comCnt, "무", noneCnt, "패", userCnt)
    print("※※※※※※※※※※※※※")


comCnt = 0
userCnt = 0
noneCnt = 0

while(1) :
    games = input("몇 판을 진행하시겠습니까? : ")
    try:
         games = int(games)
         playGame(games)
         break
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => "+games+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
