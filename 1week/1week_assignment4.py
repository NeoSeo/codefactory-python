
#다이아몬드 그리기
#00100
#01110
#11111
#01110
#00100


for b in range(3, 6):
    print("0" * (5-b) + "1" * (b-(5-b)) + "0" * (5-b))
for a in range(1, 3):
    print("0" * a + "1" * (5-2*a) + "0" * a)


print("          ")

for a in range(1, 6):
    a = a - 3
    if a < 0:
        a = -a
    print("0" * a + "1" * (5 - a  * 2) + "0" * a)
