#연봉 계산기
def calcSalary(salary) :
    #연봉 테이블 선언
    salaryTable = {"1200":6, "4600":15, "8800":24, "15000":35, "30000":38, "50000":40}
    #연봉테이블 키 조회
    salaryKeys = list(salaryTable.keys())
    #기타 세율 선언
    tax = 42
    for x in salaryKeys :
        #연봉구간 비교
        if(int(x) >= salary):
            tax = salaryTable[x]
            break
    print()
    print("※※※※연봉계산※※※※")
    print("▶세     율 :",tax,"%")
    print("▶세전 연봉 :",salary,"만원")
    print("▶세후 연봉 :", int(salary - (salary/100*tax)),"만원")
    print("※※※※※※※※※※※※")

salary = int(input("월급을 입력해주세요.(만원 단위 입력)(ex= 300) => "))
calcSalary(salary*12)
