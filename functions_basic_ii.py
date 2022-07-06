#1

def countdown(num):
    newarray = []
    for i in range(num,-1,-1):
        newarray.append(i)
    return newarray
print(countdown(5))

#2
def print_and_return(num1,num2):
    print(num1)
    return num2
print(print_and_return(1,2))

#3
def first_plus_length(array):
    x = array[0] + len(array)
    return x
print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(array):
    count = 0
    newarray = []
    for i in range(len(array)):
        if len(array) < 2:
            return False
        elif array[i] > array[1]:
            newarray.append(array[i])
            count += 1
    print(count)
    return newarray
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


#5
def length_and_value(size,value):
    newarray = []
    for i in range(size):
        newarray.append(value)
    return newarray
print(length_and_value(4,7))
print(length_and_value(6,2))



