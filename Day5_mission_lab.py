# 1) Integer and float.
# 2) Integer.
# 3)
pi = 3.14
radius = 2
area = pi * (radius ** 2)

print(area)

# 4)
name = 'Yun'
surname = 'Chang'
# i) string
# ii)
print (name + ' ' + surname)
# iii)
print(name.lower() + ' ' + surname.upper())

# 5)

question = input('Is basic training difficult (y or n)? ')
if question == 'y':
    print('You are strong!')
else:
    print('You are very strong!')

# 6)
budget = int(input('What is you budget for food this month? '))

if budget <= 0 or budget > 1000:
    print('error')
elif budget > 550:
    print('You will eat well this month!')
elif budget < 550:
    print('This is less than the average American food budget')
else:
    print('This is the average American food budget')
print('***********')
# 7)
x = 2
while x <= 100:
    print(x)
    x = x + 2
print('***********')
for x in range(2, 101,2):
    print(x)
print('***********')
# 8)
import random
nums = []
for x in range(100):
    y = random.randint(1, 100)
    nums.append(y)
print(nums)