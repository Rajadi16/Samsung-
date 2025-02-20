number1 = input("Enter the number: ")
list1 = []
list2=[]
for i in number1:
    list1.append(i)
list1.reverse()
number2 = "".join(list1)
if int(number1) < int(number2):
    print(number2, "is the second smallest bigger number")
else:
    for i in len(number1):
        for j in range(2**(len(number1)-1)):
            list2.append(number1[i]+number1[j]+number1[j+1])
    
