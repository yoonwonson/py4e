# 나이와 버스 요금 입력받기
age = input("나이를 입력하세요: ")
pay = input("카드/현금 ")
age = int(age)

# 버스 요금을 알아내는 함수
def bus_fare(age, payment):
    if payment == '카드':
        if age < 8:
           return '무료'
        elif age < 14:
            return '450원'
        elif age < 20:
            return '720원'
        elif age < 75:

            return '1200원'
        else :
            return '무료'
    else:
        if age < 8:
               return '무료'
        elif age < 14:
            return '450원'
        elif age < 20:
            return '1000원'
        elif age < 75:
            return '1300원'
        else :
            return '무료'

print('나이:',age)
print('지:',pay)
print('버스요금:',bus_fare(age, pay))
