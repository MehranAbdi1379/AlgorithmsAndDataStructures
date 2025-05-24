input_number = input("Enter a number: ")

while len(input_number) > 1:
    sum = 0
    for num in input_number:
        sum += int(num)
    input_number = str(sum)
print(input_number)
