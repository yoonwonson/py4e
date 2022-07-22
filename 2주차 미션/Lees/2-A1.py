import random

def calcRsp(rsp, computer) :
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
            elif (minus == 0) :
                result = "비김!"
            else :
                result = "컴퓨터 승리!"

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

rsp = str(input("가위/바위/보를 입력하세요.(가위:0, 바위:1, 보:2) => "))
computer = random.randint(0, 2)
calcRsp(rsp, computer)
