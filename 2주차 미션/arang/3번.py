name = input('학생 이름을 입력해주세요')
score = int(input('점수를 입력해주세요'))

def grader(name,score) :
    if score<60 :
        return 'F'
    elif score<=64 :
        return 'D'
    elif score<=69 :
        return 'D+'
    elif score<=74 :
        return 'C'
    elif score<=79 :
        return 'c+'
    elif score<=84 :
        return 'B'
    elif score<=89 :
        return 'B+'
    elif score<=94 :
        return 'A'
    else :
        return 'A+'

print('학생이름:',name)
print('점수 :',score,'점')
print('학점 :',grader(name,score))
