number = [int(x) for x in input("enter the number")]  
total = 0  

for i in range(len(number)):
    if number[i] % 2 != 0:
        if i % 2 == 0:  
            total += number[i]

print(total)

