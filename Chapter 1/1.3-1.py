# 1
x = None
y = False
z = True

result = x or y and z
print(result)  # False

# 2
s = "abcdefghijklmn"
print(s[::-2][2:6])  # jhfd

# 3
a = 53
b = 14

result = ((a % b) * (b // 5)) - (a // b)
print(result)  # 22 - 3 = 19

# 4
x = [1, 2, 3]
y = [1, 2, 4]

print(x < y and y != x or x == y)  # True

# 5
a = [256]
b = [256]
print(a == b, a is b)  # True, False

x = 256
y = 256
print(x == y, x is y)  # True, True

# 6
a = {1, 2, 3, 5}
b = {2, 3, 4}
c = {3, 4, 5}

print((a & b) ^ (b & c))  # {2,3} ^ {3,4} = {2,4}

# 7
lst = list("hello")
lst[1:4] = "i"
print("".join(lst))  # hio

# 8
a = 0
b = "0"
c = []

result = a or b and c or b
print(repr(result))

# 9
x = 5  # 0b0101    100
y = 3  # 0b0011    110

print((x & y) << 2 | (x ^ y))  # 110 = 6

# 10
a = "Python"
b = [1, 2, 3]
c = {1, 2, 3}
d = {"a": 1}

print(len(a) * (b[1] in c) + (3 in d))  # 6
