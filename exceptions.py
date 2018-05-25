#exceptions

def divide(first, second):
    try: #예외, 에러 처리!
        return first / second
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

print(divide(2,2))
print(divide(4,0))

#Exception class!
class EvenNumberDivisionError(Exception):
    pass #아직 구현되지 않은 부분은 지나가도록 한다

def devide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDivisionError #raise 일으키다
    else:
        return first / second

print(devide_by_odd_number(6,3))
print(devide_by_odd_number(6,2))
