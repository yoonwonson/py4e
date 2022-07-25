#연봉 계산기
def calcGrade(name, score) :
    #연봉 테이블 선언
    gradesTable = {"95":"A+", "90":"A", "85":"B+", "80":"B", "75":"C+", "70":"C", "65":"D+", "60": "D"}
    #연봉테이블 키 조회
    gradesKeys = list(gradesTable.keys())
    #기타 세율 선언
    grades = "F"
    for x in gradesKeys :
        #연봉구간 비교
        if(int(x) <= score):
            grades = gradesTable[x]
            break
    print()
    print("※※※※학점계산※※※※")
    print("▶학생이름 :", name)
    print("▶점    수 :", score," ")
    print("▶학    점 :", grades)
    print("※※※※※※※※※※※※")

name = str(input("이름을 입력해주세요.(ex=홍길동) => "))
while (1):
    score = input("점수를 입력해주세요.(ex=1~100) => ")
    #예외 처리
    try:
         score = int(score)
         calcGrade(name, score)
         break
    except Exception as e:
        print()
        print("※※※※※※※입력오류※※※※※※※")
        print("숫자를 입력해주세요.(입력값 => "+score+")")
        print("※※※※※※※※※※※※※※※※※※")
        print()
        continue
