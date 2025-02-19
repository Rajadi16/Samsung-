number1 = input("Enter the number: ")
list1 = []
for i in number1:
    list1.append(i)
list1.reverse()
number2 = "".join(list1)
if int(number1) < int(number2):
    print(number2, "is the second smallest bigger number")
else:
    print("no number exist")
