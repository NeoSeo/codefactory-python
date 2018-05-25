
def multiple():
    try:
        dan = int(input("구구단을 입력하시오 "))
        if dan > 1 and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2에서 9사이의 숫자만!")
            multiple()
    except ValueError:
        print("숫자만 입력해 주세요 ")
        multiple()
    except:
        print("알 수 없는 에러가 발생 했습니다.")
        multiple()
multiple()



#############   2~9라는 숫자 외에는 구구단이 출력하지 않도록 처리했습니다
#############   예를 들어, 현재 숫자가 아닌 "1단"이라는 문자를 넣으면 구구단이 실행되지 않고 종료됩니다.
#############   잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력해주세요."이라는 문구와 함께 다시 구구단이 실행되도록 합시다.
