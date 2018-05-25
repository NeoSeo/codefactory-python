
class School:
        def __init__(self, name, year, address):
            self.name = name ="서강대ㅎㅎ"
            self.year = year #값이 지정되어 있지 않다.
            self.address = address

call = School("서강대", "1960", "서울시 마포구")
#실행해 보면 name는 서강대ㅎㅎ로, 나머지는 1960, 서울시 마포구로 나온다.
#함수 안의 값 지정이 강력하나, 그래도 위의 call = School("서강대", "1960", "서울시 마포구") 가 없으면
#에러가 난다. 왜일까?

print(call.name)
print(call.year)
print(call.address)
