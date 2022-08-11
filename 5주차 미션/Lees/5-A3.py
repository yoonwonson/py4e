import random

def randomNumber() :
    number = []
    while len(number) != 3 :
        no = random.randint(0, 100)
        if (no in number) :
            continue
        number.append(no)
    number.sort()
    return number

def checkNumber(list, num) :
    try :
        return list.index(num)
    except Exception as e:
        return -1

def hint(list, num) :
    if (num < list[0]) :
        return 0
    elif ( list[0] < num < list[1]) :
        return 1
    elif ( list[1] < num < list[2]) :
        return 2
    elif ( list[2] < num) :
        return 3

resultMsg = ["최솟값", "중간값", "최댓값"]
hintMsg = ["최솟값보다 작습니다", "최소값 보다 크며 중간값 작습니다", "중간값 보다 크며 최댓값 보다 작습니다.", "최댓값 보다 큽니다."]
numberlist = randomNumber()
result = []
no = 1
while(1) :
    print(no,"차 시도")
    num = input("숫자를 예측해보세요 : ")
    try:
        num = int(num)

        if (num in result) :
            print("이미 예측에 사용한 숫자입니다")
            print()
            continue

        res = checkNumber(numberlist, num)

        if (res > -1) :
            print("숫자를 맞추셨습니다!",num,"은",resultMsg[res],"입니다.")
            print()
            result.append(num)
            if (len(result) == 3) :
                print(no,"번 시도만에 예측 성공")
                print("게임종료")
                break

        if (no % 5 == 0) :
            print(num,"은", hintMsg[hint(numberlist, num)])
        no = no + 1
        print()


    except Exception as e:
        print(e)
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => ",num,")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
