def wrongGuestBook(guestBook) :
    print("\n※※※※※※※잘못 입력 찾기※※※※※※※")
    f = open("./4-A3.txt", 'w')
    f.write(guestBook)
    f.close()
    for i in guestBook.split('\n') :
        j = i.split(",")
        if (len(j[1]) != 13) or (len(j[1].split("-")) != 3) or (not j[1].startswith("010")) :
            print("▶ 잘못 쓴 사람 :", j[0])
            print("▶ 잘못 쓴 사람 번호 :", j[1])
            print()
    print("※※※※※※※※※※※※※※※※※※")

guestBook = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrongGuestBook(guestBook)
