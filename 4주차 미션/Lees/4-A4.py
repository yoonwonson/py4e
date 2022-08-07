def checkId(id) :
    print("\n※※※※※※※주번검증※※※※※※※")
    gender = ""
    if (id[6] != "-") or (len(id) != 14) :
        print("▶ 잘못된 번호입니다.")
        return

    if (id[7] == "1" or id[7] == "3") :
        gender = "남자"
    elif (id[7] == "2" or id[7] == "4") :
        gender = "여자"
    else :
        print("▶ 잘못된 번호입니다.")
        return

    if ( 21 >= int(id[0:2]) >= 0) :
        print("▶ 2000년 이후 출생자.")

    print("▶ "+id[0:2]+"년"+id[2:4]+"월", gender)


    print("※※※※※※※※※※※※※※※※※※")

while(1) :
    id = input("주민번호를 입력하세요. : ")
    try:
        int(id[0:6])
        int(id[7:14])
        checkId(id)
        break
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("주민번호를 정확하게 입력해주세요.(입력값 => "+id+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
