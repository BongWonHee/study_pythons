# slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# type(thislist) 타입확인.
# <class 'list'>
# len(thislist)
# 7
# thislist[1:3] 1부터 3전까지확인
# ['banana', 'cherry']
# thislist[:-1] 뒤에서 1자리빼고 확인
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

# change value in list 
# thislist[1] = 'watermelon' thislist 내부 인덱스 변경
# thislist[1:3] = ['cherry', 'watermelon'] 내부 인덱스2개 변경

#sort
# thislist.sort() 내부 인덱스 정렬
# thislist.sort(reverse=True) 내부 인덱스 역정렬

# 붙여넣기
thislist = ["apple", "banana", "cherry"]
# thislist.append('melon') melon을 뒤에서 부터 추가하기

# thislist.pop() 뒤에서 부터 자료 빼기.
# 'orange'
# 초기화 방식
# thislist =[]
# thislist = list()

#casting
# words = str()

pass
