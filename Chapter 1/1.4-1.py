for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(f"{i}-{j}")

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

a = True
b = False
c = True

if a and b or c:
    print("Yes")
else:
    print("No")
