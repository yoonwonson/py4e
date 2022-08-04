def makeNum(num) :
    print("\n※※※※※※※숫자변환※※※※※※※")
    result = ""
    index = 0
    strNum = str(num)
    while index != len(strNum) :
        if (index % 3 == 0 and index != 0) :
            result = strNum[len(strNum)-1-index] + "," + result
        else :
            result = strNum[len(strNum)-1-index] + result
        index = index + 1
    print("▶ 숫자는 :",result)
    print("※※※※※※※※※※※※※※※※※※")

while(1) :
    num = input("숫자를 입력하세요.(ex= 1000) => ")
    try:
         num = int(num)
         makeNum(num)
         break
    except Exception as e:
        print(e)
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => ",num,")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
