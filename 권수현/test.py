from itertools import product

buttons = sorted(list({'0','1','2','3','4','5','9'}))
for repeat in range(1,4):
    for idx in product(buttons,repeat=repeat):
        num=''.join(idx)


list = ['a','b','c']
dic = {key : 0 for key in list}
print(tuple(dic.items()))

key = ['a','b','c']
value = [1,2,3]
dic = dict(zip(key,value))
print(dic)