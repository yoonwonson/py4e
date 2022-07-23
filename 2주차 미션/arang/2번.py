try :
    MonthlyPayment = int(input("월급을 입력해주세요(만 단위)."))
except :
    print('숫자를 입력해주세요.')
    quit()

YearlyBefore = MonthlyPayment*12

print('세전연봉',YearlyBefore)

if YearlyBefore<=1200 :
    print('세후연봉',YearlyBefore*0.94)
elif YearlyBefore<=4600 :
    print('세후연봉',YearlyBefore*0.85)
elif YearlyBefore<=8800 :
    print('세후연봉',YearlyBefore*0.76)
elif YearlyBefore<=15000 :
    print('세후연봉',YearlyBefore*0.65)
elif YearlyBefore<=30000 :
    print('세후연봉',YearlyBefore*0.62)
elif YearlyBefore<=50000 :
    print('세후연봉',YearlyBefore*0.60)
elif YearlyBefore>50000 :
    print('세후연봉',YearlyBefore*0.58)
