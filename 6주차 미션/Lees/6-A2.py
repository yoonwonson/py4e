from collections import deque

member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

dict = {}
list = []
for idx, val in enumerate(member_names):
    score = 0
    for i, v in enumerate(member_records[idx]):
        score = score + v
    score = score/len(member_records[idx])
    list.append({"이름":val, "실적":f"{score:.2f}"})
list = sorted(list, key=lambda member:(member['실적']), reverse=True)

bonus = []
bonusCnt = 0
counsel = []
counselCnt = 0
for idx, val in enumerate(list):
    if (float(list[idx]['실적']) > 5 and bonusCnt < 2) :
        bonus.append(list[idx]['이름'])
        bonusCnt = bonusCnt + 1
    if (float(list[idx]['실적']) < 3) :
        counsel.insert(0, list[idx]['이름'])
        counselCnt = counselCnt + 1

for val in bonus :
    print("보너스 대상자 "+ val)

for val in counsel :
    print("\n면담 대상자 "+ val)
