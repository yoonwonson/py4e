def free() :
    return '지불유형 무관하게 무료입니다'
def old() :
    return '나이 :'
def pay() :
    return '지불유형 :'
def fare() :
    return '버스요금 :'

try :
    age = int(input('당신의 나이는?'))
except :
    print('숫자를 입력해주세요')
    quit()

if age<8 :
    print(old(),age)
    print(free())
elif age<14 :
    method = str(input('결제수단은 무엇입니까? 카드 또는 현금으로 대답해주세요'))
    print(old(),age)
    print(pay(),method)
    if method=='현금' :
        print(fare(),'450원')
    elif method=='카드' :
        print(fare(),'450원')

elif age<20 :
    method = str(input('결제수단은 무엇입니까? 카드 또는 현금으로 대답해주세요'))
    print(old(),age)
    print(pay(),method)
    if method=='현금' :
        print(fare(),'1000원')
    elif method=='카드' :
        print(fare(),'720원')

elif age<75 :
    method = str(input('결제수단은 무엇입니까? 카드 또는 현금으로 대답해주세요'))
    print(old(),age)
    print(pay(),method)
    if method=='현금' :
        print(fare(),'1300원')
    elif method=='카드' :
        print(fare(),'1200원')

else :
    print(old(),age)
    print(free())
