#예외처리
try: 
    age = input("나이를 입력하세요: (ex.30) => ")
except :
    print('숫자를 입력해주세요')
    quit()

# 나이와 버스 요금 입력받기
pay = input("결제수단을 입력하세요 (ex. 카드/현금) =>  ")
age = int(age)

# 버스 요금을 알아내는 함수
def busFare(age, payment):
    if payment == '카드':
        if age < 8 or age >= 75 :
           return '무료'
        elif age >= 20 : 
            return '1200원'
        elif age >= 14 :
            return '720원'
        elif age >= 8 :
            return '450원'
    
    else:
        if age < 8 or age >= 75 :
               return '무료'
        elif age >= 20 : 
            return '1300원'
        elif age >= 14 :
            return '1000원'
        elif age >= 8 :
            return '450원'

print('나이:',age)
print('지불유형:',pay)
print('버스요금:',busFare(age, pay))
