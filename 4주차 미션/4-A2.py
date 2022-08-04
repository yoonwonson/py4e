def countWord(txt, word) :
    print("\n※※※※※※※문자찾기※※※※※※※")
    f = open("./4-A2.txt", 'w')
    f.write(txt)
    f.close()
    count = 0
    txtLen = len(txt)
    wordLen = len(word)
    findTxt = 0
    while (findTxt + txtLen >= txtLen) :
        findTxt = txt.find(word)
        if (findTxt > 0) :
            count = count + 1
            txt = txt[findTxt+wordLen : txtLen]
        elif (findTxt == -1) :
            break
    print("▶ '"+word+"' 갯수는 :",count)
    print("※※※※※※※※※※※※※※※※※※")

while(1) :
    txt ="""안녕하세요.
        반갑습니다. 파이썬 공부는 정말 재밌습니다.
        """

    word = str(input("찾을 문자를 입력하세요.(ex= 습니다) => "))
    try:
         countWord(txt, word)
         break
    except Exception as e:
        print(e)
        print()
