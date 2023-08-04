thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for item in items:
#     pass
#for문은 리스트 형태를 돌리때쓴다.
for fruit in thislist:
    print(fruit)
pass

# range(2, 10)

for i in range(2,10):
    print(i)

# while
first = 3
while (first < 6):
    pass
    print('while count{}'.format(first))
    first = first + 1

# list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)
pass

# next(fruits_enumerate)
# (0, 'apple')
# next(fruits_enumerate)
# (1, 'banana')
# next(fruits_enumerate)
# (2, 'cherry')
# next(fruits_enumerate)
# (3, 'orange')
# next(fruits_enumerate)
# (4, 'kiwi')
# next(fruits_enumerate)
# (5, 'melon')
# next(fruits_enumerate)
# (6, 'mango')
# next(fruits_enumerate)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# StopIteration

# list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)
for index_fruit in fruits_enumerate: # 튜플 묶음
    print(index_fruit)
    pass

fruits_enumerate = enumerate(fruits)
fruit_print_format ="number : {0}, fruit name : {1}"
for (index, fruit) in fruits_enumerate: # 튜플 분리
    print(fruit_print_format.format(index, fruit))
    pass
pass