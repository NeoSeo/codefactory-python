#한식, 중식, 일식을 고르고 그 중에 그러면 해당하는 식당 임의 추천
import random

list1 = ["한정식", "불고기 덮밥", "돌솥밭", "삼겹살"]
list2 = ["짜장면", "양꼬치", "팔보채", "홍콩요리"]
list3 = ["스시집", "일본카레", "오코노미야끼", "덴뿌라"]

call = input("한식, 중식, 일식 중 고르시오 ")

if call == "한식":
    print(random.choice(list1))
#    print(random.randint(0, len(list1))) randint는 리스트 순서열에 따른 랜덤 선택, len은 리스트 길이
elif call == "중식":
    print(random.choice(list2))
elif call == "일식":
    print(random.choice(list3))
else:
    print("한식, 중식, 일식 중에서 선택!")
    pass
