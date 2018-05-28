##### Article variables
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업은 쉬워요"
view_count3 = 0
# 이런 것을 하나하나 계속 지정한 다면 번거롭다!


class Article: #설계 도면
    title = "개발"
    author = "마르코"
    content = "개발은 쉬워요"
    view_count = 0

article1 = Article() #class는 대개 대문자로 시작, 설계도에 접근가능한 객체를 만들었다.
print(article1.title)
article2 = Article() #class 값은 외부에서 다른 값을 지정해도 영향, 변경 안된다.
print(article2.author)


class Article2:
    author = "marco"
    view_count = 0

    def __init__(self, title, content): # __init__과 self는 항상 같이 쓰인다, self는 class 안의 함수에 접근하겠다 선언
        self.title = title1
        self.content = content2 #위의 content2로 지정해도 함수 밖에서 실행하면 외부의 지원이 끊겨 밑에서 새로 지정해야 한다?

    def read(self):
        self.view_count = self.view_count + 1 #글을 읽을 때마다 조회수 1씩 올라가게 하기

article3 = Article2("창업", "창업이 쉬울까") #이게 없으면 위의 class 실행시 오류
print(article3.title)
print(article3.content)
print(article3.view_count)
article3.read() #누가 한 번 읽음
# article1.view_count1 = article1.view_count + 1 만약 class가 없다면 이런 번거러움 작업을 함..
print(article3.view_count)

#### class 상속!!! ######
class BrunchArticle(Article2): #article class 전체를 복사 붙이기
    source = "brunch"

    def read(self): #over write 다른 class에서 가져온 함수에 변경하는 행위
        self.view_count = self.view_count + 2 #글을 읽을 때마다 조회수 2씩 올라가게 하기


brunch_article = BrunchArticle("통일", "개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
