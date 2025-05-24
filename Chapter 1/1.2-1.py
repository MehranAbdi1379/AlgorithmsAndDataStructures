text = input("Please enter the text: ")

polishedText = ""

for char in text:
    if char.isalpha():
        polishedText += char.lower()

reversedText = ""

for i in range(len(polishedText) - 1, -1, -1):
    reversedText += polishedText[i]

if reversedText == polishedText:
    print("Yes")
else:
    print("No")
