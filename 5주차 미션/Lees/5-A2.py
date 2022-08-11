s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
a = [3,2,4,2,5,2,4,3,1,2]

grader = []
for i in s :
    row = i.split(",")
    result = list(row[1])
    score = 0
    for j in range(10) :
        if (int(result[j]) == a[j]) :
            score = score + 10
    grader.append(str(score)+","+row[0])

grader.sort(reverse=True)

no = 0
for i in grader :
    no = no + 1
    result = i.split(",")
    print("학생:" + result[1] + " 점수:" + result[0] + "점 " + str(no)+ "등")
