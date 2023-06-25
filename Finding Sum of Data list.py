import re
 
numbers = open('regex_sum_1812343.txt')
numlist = list()
for line in numbers:
    line = line.strip()
    nums = re.findall('[0-9]+', line)
    numlist = numlist + nums

sum = 0
for number in numlist:
    sum = sum + int(number)


print(sum)


