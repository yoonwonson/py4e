try :
    age = int(input('당신의 나이는?'))
except :
    print('숫자를 입력해주세요')
    quit()

method = str(input('결제수단은 무엇입니까? 카드 또는 현금으로 대답해주세요'))

def busFare(age,method) :
    if age<8 or age>=75 :
        return '무료'
    if age<14 :
        return '450원'
    if age<20 :
        if method=='현금' :
            return '1000원'
        if method=='카드' :
            return '720원'
    if age<75 :
        if method=='현금' :
            return '1300원'
        if method=='카드' :
            return '1200원'
            
print('나이:',age)
print('지불유형 :',method)
print('버스요금 :',busFare(age,method))
