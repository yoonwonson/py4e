
# 입력
while True :
    try :
        number = int(input("몇 단? : "))
        break
    except :
        print("숫자를 입력해주세요")
        continue

#구구단 함수
def gugudan(number) :
    zork = -1
    value = 1 * number
    while True :
        if value <= 50 :
            zork = zork + 2
            value = number * zork
            if value <= 50 :
                 print(number,'X',zork,'=',value)
            else :
                break
    print('끝!')


# 출력
print('몇 단? :',number)
print(number,'단')
(gugudan(number))
