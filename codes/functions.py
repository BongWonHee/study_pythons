# package == module(python)

#기본적이 function구성
def function_name() : 
    pass
    return 0

function_name()
pass

# 평범한 params  이용한 결과값 받기
def add(first, second) :
    sum = first + second
    return sum

resultsum = add(4, 6)
pass

# set defualt value with params
def minus(first, second = 0): #second에 0 이라는 기본값 할당
    result = first - second
    return result

minus(3, 5)
minus(3)

# return tuple datatype
def multiply(first, second = 1) :
    multiply = first * second
    return (multiply,first,second)

result_tuple = multiply(3,4)
multiply,first,second = multiply(4)
# TypeError: 'int' object is not callable
# _ <-- 쓰지않는 변수, _result <-- 내부에서 쓰는 변수 라는 의미로 _ 를 사용한다.
result_multiply, result_first, result_second = multiply(4)
pass