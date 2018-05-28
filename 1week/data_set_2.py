print("dict part")
print("dict에선 반드시 큰따옴표를 붙여야한다")
dict_b={
"apple" : "a thing to eat",
"dog" : "my lovely animal"
}
print(dict_b)
print(dict_b["dog"])

print("set part 수학의 집합과 동일")
set_a=set([1,2,3])
set_b=set([3,5,6])
print(set_a)
print(set_b)
print(set_a&set_b, "교집합")
print(set_a|set_b, "합집합")
print(set_a-set_b, "차집합")
