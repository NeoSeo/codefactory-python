for num in range(1, 10):
    print(num) #10은 포함 안 한다.

num_list = [1,2,3,4,5,6,7,8,9] #for는 list나 tuple을 받고 dict는 형태가 좀 다르다.
for num in num_list:
    print(num)

#while은 무한루프 형태, 참일 때 무한으로 돌린다.
a = 1
while a < 10:
    print(a)
    a = a + 1
