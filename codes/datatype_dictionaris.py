# 초기화 방법
thisdict = {} # empty inital
thisdict = dict() # empty inital

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# len(thisdict)
# 3
# type(thisdict)
# <class 'dict'>
# special variables
# function variables
# thisdict['model']
# 'Mustang'
# thisdict['brand'] = 'yojulab'
# thisdict.keys()
# dict_keys(['brand', 'model', 'year'])
# type(thisdict.keys())
# <class 'dict_keys'>
# thisdict.values()
# dict_values(['yojulab', 'Mustang', 1964])
# add item in dict 키값이 없으면 추가 있으면 변경됨.
# thisdict['color'] = 'Red'
# remove item 뒤쪽에 키값을 지정하지 않으면 전체 삭제됨.
# del thisdict['year']

dict_format = "key : {0}, value : {1}"
for key, value in thisdict.items():
    print(dict_format.format(key, value))
    pass
pass

