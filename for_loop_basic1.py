#1
for i in range(151):
    print(i)

#2 
for i in range(5,1001):
    if i%5 == 0:
        print(i)

#3
for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

#4
sum = 0
for i in range(500001):
    sum += i

print(sum)

#5
count = 2018
while count > 0:
    print(count)
    count -= 4

#6 
lowNum = 2
highNum = 9
mult = 3 
for i in range(lowNum,highNum + 1):
    if i%mult == 0:
        print(i)

