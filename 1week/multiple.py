number = int(input("몇 단을 원하십니까?"))

a = 1
while a<10:
  print(a*number)
  a = a + 1

b = [1,2,3,4,5,6,7,8,9]
for num in b:
    print(num*number)

#아니면 for num in range(1, 10): 을 써도 괜찮다.

for nam in range(1, 10):
    print("{} * {} = {}".format(nam, number, nam*number))
    
