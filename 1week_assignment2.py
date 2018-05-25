class Person:
    def __init__(self, name, age, sex): #init은 실행시 입력을 받으라는 선언
        self.name = name
        self.age = age
        self.sex = sex

class Company(Person):
    #status = "대리"

    #기존 클래스를 상속하되 주소를 변경하지 않고, 직급을 입력하여 추가할 수 있도록 하자
    def __init__(self, name, age, sex, status   ):
        super().__init__(name, age, sex) #super는 상속 받은 클래스의 주소를 변수로 그대로 가져오는 명령어
        self.status = status


peer = Company("용", 20, "남", "대리")
#print(peer.name)
print(peer.__dict__) #__dict__는 class 안에 주소를 dictionary 형태로 보여준다.

#info = Person(input("이름입력하세요 "),input("나이입력하세요 "), input("성별? "))
#print("이름은 " + info.name)
#print("나이는 " + info.age)
#print("성별은 " + info.sex)
#info2 = Company(input("이름? "),input("나이? "), input("성별? "))
#print(info2.status)
