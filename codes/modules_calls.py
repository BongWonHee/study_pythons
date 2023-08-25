# 기본 import 하는법
import modules 

result_sum = modules.add(8,1)

# import후 alias사용하는 법
import modules as mdls
result_sum = mdls.add(8,1)

# 파일안에 오브젝트가 있을때 import하는법
from modules import person1 as ps
print(ps['country'])

pass

