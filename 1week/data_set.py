
print("list는 벡터 안을 변경 가능하다")
a=list([1,2,3])
print(type(a))
print(a[0:2])
a.append(4)
print(a)
a.remove(3)
print(a)

print("tuple은 벡터 안을 변경 하지 못하여 상수를 쓰고 싶을 때 쓴다")
print(tuple((1,2,3)))
print("b=tuple(1,2,3)일 때, b.append 따위 못 쓴다")
