# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# key = input("Loop count : ")
# while (key !='Q'):
#     fruits_enumerate = enumerate(fruits)
#     fruit_print_format ="number : {0}, fruit name : {1}"
#     for (index, fruit) in fruits_enumerate: # 튜플 분리
#         if (int(key) > index):
#             print(fruit_print_format.format(index, fruit))
#             key = input("Loop count : ")
#         pass
# 입력한 숫자만큼만 과일을 숫자와 출력을 하고 Q를 입력하면 빠져나오는 코드.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

while True:
    key = input("Loops count: ")

    if key.upper() == 'Q':
        break
    try:
        key = int(key)
        if key <= 0:
            print("다시 입력하세요.")
        else:
            for i in range(min(key, len(fruits))):
                print(f"{i + 1}. {fruits[i]}")
    except ValueError:
        print("올바른 숫자나 'Q'를 입력하세요.")