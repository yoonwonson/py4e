def make_comma(number) :
    number = str(number)
    length = len(number)
    n = -3
    a = 1
    zork = 0
    number_ = list(number)
    while True :
        if length > n*-a :
            new_number = number_.insert((n*a)-zork,',')
            a = a+1
            zork = zork + 1
        else : 
            break
    print(('').join(number_))

number = input('숫자를 입력하세요')
make_comma(number)
