# 월급 입력받기
from tkinter import E


monthly=input('월급을 입력하세요(만 단위): ')
monthly=int(monthly)

def yearly(a):
    if a * 12 < 1200 :
        return a * 12 * (100 - 6) / 100
    elif a * 12 < 4600 :
        return a * 12 * (100 - 15) / 100
    elif a * 12 < 8800 :
        return a * 12 * (100 - 24) / 100
    elif a * 12 < 15000 :
        return a * 12 * (100 -35) / 100
    elif a * 12 < 30000 :
        return a * 12 * (100 - 38) / 100
    elif a * 12 < 50000 :
        return a * 12 * (100 - 40) / 100
    else :
        return a * 12 * (100 - 42) / 100

print('세전 연봉:',monthly * 12,'만원')
print('세전 연봉:',int(yearly(monthly)),'만원')

