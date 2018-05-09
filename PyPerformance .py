'''
python代码进行性能测试
http://python3-cookbook.readthedocs.io/zh_CN/latest/c14/p13_profiling_and_timing_your_program.html
'''

## 使用cProfile模块
# import time
# import cProfile
# def func(n):
# 	while n>0:
# 		print('times-%s'%n)
# 		time.sleep(1)
# 		n-=1

# if __name__=='__main__':
#     cProfile.run('func(10)')

# # 使用timeit模块
# from timeit import timeit
# #比较以下两种模式的时间消耗
# print(timeit('math.sqrt(2)','import math'))

# print(timeit('sqrt(2)','from math import sqrt'))

# # 构造一个计算时间的装饰器
# from functools import wraps
# import time

# def timeit(func):
# 	@wraps(func)
# 	def wrappers(*args,**kwargs):
# 		start=time.time()
# 		print('start-time',start)
# 		r=func(*args,**kwargs)
# 		end=time.time()
# 		print('end-time',end)
# 		print('{}.{}:{}'.format(func.__module__,func.__name__,end-start))
# 		return r
# 	return wrappers

# @timeit
# def countname(n):
# 	while n>0:
# 		print(n)
# 		n-=1
# 		time.sleep(0.8)

# countname(10)
