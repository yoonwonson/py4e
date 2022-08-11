def afterDay(mm,dd,day) :
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    weeks =["일","월","화","수","목","금","토"]

    rMm = 0
    rDd = days[mm-1] - dd + 1

    for i in range(mm, 12) :
        if (rDd + days[i] <= 100) :
            rDd = rDd + days[i]
            continue
        else :
            rDd = 100 - rDd
            rMm = i+1
            break
    print(str(mm)+"월 "+str(dd)+"일 "+str(day)+"요일부터 100일 뒤는 "+str(rMm)+"월 "+str(rDd)+"일 "+weeks[weeks.index(day)+1]+"요일")


mm = 0
dd = 0
day = ""

while(1) :
    mm = input("현재 월을 입력하세요 : ")
    try:
         mm = int(mm)
         break
    except Exception as e:
         print()
         print("※※※※※※※입력오류※※※※※※※")
         print("현재 월을 입력해주세요.(입력값 => "+mm+")")
         print("※※※※※※※※※※※※※※※※※※")
         print()
while(1) :
    dd = input("현재 일을 입력하세요 : ")
    try:
         dd = int(dd)
         break
    except Exception as e:
         print()
         print("※※※※※※※입력오류※※※※※※※")
         print("현재 일을 입력해주세요.(입력값 => "+dd+")")
         print("※※※※※※※※※※※※※※※※※※")
         print()
while(1) :
    day = input("현재 요일을 입력하세요 : ")
    try:
         day = day
         weeks =["일","월","화","수","목","금","토"]
         weeks.index(day)
         break
    except Exception as e:
         print()
         print("※※※※※※※입력오류※※※※※※※")
         print("요일을 입력해주세요.(입력값 => "+day+")")
         print("※※※※※※※※※※※※※※※※※※")
         print()

afterDay(mm,dd,day)
