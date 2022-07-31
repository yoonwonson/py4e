def calc(n, m) :
    print("\n※※※※※※※출  력※※※※※※※")
    yn = False
    for i in range(n,m+1):
        if (i%2 == 0) :
            print("▶ 짝  수 :",i)

        if (not yn and i == (n+m)/2) :
            if (i%2 == 0) :
                print("▶ 중앙값 :",i)
            yn = True
    print("※※※※※※※※※※※※※※※※※※")


def inputNum(cnt) :
    while(1) :
        no = input(cnt+"번째 수입력(ex= 1) => ")
        try:
             no = int(no)
             return no
        except Exception as e:
             print()
             print("※※※※※※※입력오류※※※※※※※")
             print("숫자를 입력해주세요.(입력값 => "+no+")")
             print("※※※※※※※※※※※※※※※※※※")
             print()

while (1) :
    n = inputNum("첫")
    m = inputNum("두")
    if (n >= m) :
        print()
        print("※※※※※※※※※입력오류※※※※※※※※※")
        print("첫번째 값보다 두번째 값이 크거나 같습니다.")
        print("첫번째 값 :",n,"두번째 값 :",m)
        print("※※※※※※※※※※※※※※※※※※※※※※")
        print()
        continue
    else :
        calc(n,m)
        break
