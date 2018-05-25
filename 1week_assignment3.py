import random

game = ["가위", "바위", "보"]

rock = "바위"
sci = "가위"
paper = "보"

game_list = (   #한글을 계속 쓰다보면 에러 날 수 있어서 list의 변수로 지정시킨다.
    rock,
    sci,
    paper
)

you = 0 #승리수
com = 0 #패배수

while you < 3 and com < 3:
    x = input("{}, {}, {}: ".format(
        rock, sci, paper
    ))
    y = random.choice(game_list)
    if x == y:
        print("당신: " + x + ", 컴퓨터: " + y)
        print("비겼습니다")
    elif x not in game_list:
        print("가위, 바위, 보 중에서 고르세요")
    elif  ((x == rock and y == sci)
        or (x == sci and y == paper)
        or (x == paper and y == rock)):
        print("당신: " + x + ", 컴퓨터: " + y)
        print("이겼습니다")
        you = you + 1
    else:
        print("당신: " + x + ", 컴퓨터: " + y)
        print("졌습니다")
        com = com + 1

    print(str(you) + " : " + str(com))


if you == 3:
    print("당신이 최종 승자")
else:
    print("컴퓨터가 최종 승자")

#for you in range(0, 3):

#
#        y = random.choice(game)
#        print(x, y)
#        you = you + 1
#        com = com + 1
#        print(you)
#        print(com)
