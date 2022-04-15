a = 3 + 4
print(a)
a = b = c = 20
print(a, b, c)
a += 5
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 5
print(a, type(a))
a //= 4
print(a, type(a))
a %= 2
print(a, type(a))

a, b, c = 20, 30, 40
print(a, b, c)

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

print(a > b)
print(a < b)
a, b = 10, 10
print(a == b)
print(id(a), id(b))
print(a is b)

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(id(list2), id(list1))
print(list1 is list2)
print(list1 is not list2)