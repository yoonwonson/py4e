#버스 요금
def calcBusFee(age, payment) :
    #기본 요금 선언
    fee = 0
    #결제 수단 구분
    if (payment == "카드") :
        #카드 요금 테이블
        cardTable = {"75":0, "20":1200, "14":720, "8":450}
        cardKeys = list(cardTable.keys())
        for x in cardKeys :
            #요금 비교
            if(int(x) <= age):
                fee = cardTable[x]
                break
    else :
        #현금 요금 테이블
        cashTable = {"75":0, "20":1300, "14":1000, "8":450}
        cashKeys = list(cashTable.keys())
        for x in cashKeys :
            #요금 비교
            if(int(x) <= age):
                fee = cashTable[x]
                break
    print()
    print("※※※※요금계산※※※※")
    print("▶나     이 :",age,"세")
    print("▶지불 유형 :",payment)
    print("▶버스 요금 :",fee,"원")
    print("※※※※※※※※※※※※")

while (1):
    age = input("나이를 입력해주세요.(ex= 30) => ")
    payment = input("결제 수단을 입력해주세요.(ex= 현금/카드) => ")

    #예외 처리
    try:
         age = int(age)
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => "+age+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
        continue
    try:
        payment = str(payment)
        if (payment != "현금" and payment != "카드") :
            raise Exception()
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("현금/카드를 입력해주세요.(입력값 => "+payment+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
        continue

    calcBusFee(age, payment)
    break
