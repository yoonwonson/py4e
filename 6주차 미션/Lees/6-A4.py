info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,x,여자,경기,10"

infoList = info.split(",")
cnt = 0
nameList = []
ageList = []
telList = []
genderList = []
addrList = []
sellCntList = []

dict = {}

for idx, val in enumerate(infoList):
    print(idx, val)
    if (cnt == 0) :
        nameList.append(val)
        cnt = cnt + 1
    elif (cnt == 1) :
        ageList.append(val)
        cnt = cnt + 1
    elif (cnt == 2) :
        if (len(val) != 13) or (len(val.split("-")) != 3) or (not val.startswith("010")) :
            telList.append("010-0000-0000")
        else :
            telList.append(val)
        cnt = cnt + 1
    elif (cnt == 3) :
        genderList.append(val)
        cnt = cnt + 1
    elif (cnt == 4) :
        addrList.append(val)
        cnt = cnt + 1
    elif (cnt == 5) :
        sellCntList.append(val)
        cnt = 0


sell = tuple(sellCntList)
sell = tuple(sorted(sell, key=lambda x: int(x), reverse=True))
no = 0
selectNo = -1
while (1) :
    selectNo = sellCntList.index(sell[no])
    if (telList[selectNo] == "010-0000-0000") :
        no = no + 1
    else :
        break

dict["아이디"] = nameList
dict["나이"] = ageList
dict["전화번호"] = telList
dict["성별"] = genderList
dict["지역"] = addrList
dict["구매횟수"] = sellCntList
print("※※※※※※※출력※※※※※※※")
print(dict)
print("[할인 쿠폰을 받을 회원정보]\n▶아이디:",nameList[selectNo],"\n▶나이:",ageList[selectNo],"\n▶전화번호:",telList[selectNo],"\n▶성별:",genderList[selectNo],"\n▶지역:",addrList[selectNo],"\n▶구매횟수:",sellCntList[selectNo])
