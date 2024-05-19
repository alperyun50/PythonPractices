squared = lambda num: num * num

 # def squared(num): 
 #   return num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(12))

sum = lambda a, b: a + b

print(sum(10, 5))

######################################
def funcbuilder(x):
    return lambda num: num + x

addTen = funcbuilder(10)
addTwenty = funcbuilder(20)

print(addTen(5))
print(addTwenty(5))

#######################################

# lambda num: num * num

numbers = [3,7,1,9,5]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

#######################################

# lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#######################################

from functools import reduce

# lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

# lambda acc, curr : acc + len(curr)

names = ["Dave Grey", "Sara Ito", "John Jacob"]

char_count = reduce(lambda acc, curr : acc + len(curr) , names, 0)

print(char_count)