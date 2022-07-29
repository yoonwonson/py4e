def calcGugu(guguNum) :
    print("\n※※※※※※※구구단※※※※※※※")
    print("▶ 단 수 :",guguNum,"단")
    value = 0
    i = -1
    while (1) :
        i = i + 2
        value = guguNum * i
        if (value >= 50) :
            break
        else :
            print("▶",guguNum,"*",i,"=",value)
    print("※※※※※※※※※※※※※※※※※※")


while(1) :
    guguNum = input("구구단을 입력하세요.(몇 단? : )(ex= 8) => ")
    try:
         guguNum = int(guguNum)
         calcGugu(guguNum)
         break
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => "+guguNum+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
