global zork
zork = 0
global No
no = 0
def count_prime_number(n, m) :
    global zork
    global no
    for thing in numbers :
        zork = zork + 1
        if thing == 1 :
            no = no + 1
        else :
            for n in range(2, thing) :
                if thing % n == 0 :
                    no = no + 1
                    break
# 입력
while True :
    try :
        n = int(input("첫 번째 수 입력 : "))
        break
    except :
        print('숫자를 입력해주세요.')
        continue

while True :
    try :
        m = int(input("두 번째 수 입력 : "))
        if m <= n :
            (print('첫 번째 수보다 큰 숫자를 입력해주세요.'))
        else :
            break
    except :
        print('숫자를 입력해주세요')
        continue
        
numbers = [ i for i in range(n, m + 1)]
count_prime_number(n, m)
print('소수 개수 :',zork-no)
