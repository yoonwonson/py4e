# 월급 입력받기
from tkinter import E


monthly=input('월급을 입력하세요(만 단위): ')
monthly=int(monthly)

def yearly(a):
    year = a * 12
    if year  <= 1200 :
        return year  * (100 - 6) / 100
    elif year  <= 4600 :
        return year  * (100 - 15) / 100
    elif year  <= 8800 :
        return year  * (100 - 24) / 100
    elif year  <= 15000 :
        return year  * (100 -35) / 100
    elif year  <= 30000 :
        return year  * (100 - 38) / 100
    elif year  <= 50000 :
        return year  * (100 - 40) / 100
    else :
        return year * (100 - 42) / 100

print('세전 연봉:',monthly * 12,'만원')
print('세전 연봉:',int(yearly(monthly)),'만원')
