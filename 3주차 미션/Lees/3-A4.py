def calc(n, m) :
    print("\n※※※※※※※출  력※※※※※※※")
    result = 0
    for i in range(n,m+1):
        if (isPrimeNumber(i)) :
            result = result + 1
    print("▶ 소수개수 :",result)
    print("※※※※※※※※※※※※※※※※※※")

def isPrimeNumber(x):
    if x == 1 :
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

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
