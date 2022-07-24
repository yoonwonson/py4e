# 이름과 점수 입력받기
name = input("이름을 입력하세요: ")
score = input("점수를 입력하세요: ")
score = int(score)

# 학점 출력 함수
def grader(name,score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 65:
        return 'D+'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 출력
print("학생 이름 :",name)
print("점수 :",score,"점")
print("학점 :",grader(name, score))
