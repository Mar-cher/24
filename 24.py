# !/usr/bin/python
# coding:utf8
'''
介绍: 24点游戏
1.24点游戏是老少皆宜的游戏，玩法很简单
1).给玩家4张牌，每张牌面值1-13之间，允许有相同的牌，
2).采用加，减，乘，除四则运算
3).允许有小数
4),可以用括号，但每张牌只能使用一次
#现在的问题在于：如何给字符串中的序列添加括号
#方法：枚举法
#4个数字和2个运算符可能组成的表达式形式
# exps = ('((%s %s %s) %s %s) %s %s',
#         '(%s %s %s) %s (%s %s %s)',
#         '(%s %s (%s %s %s)) %s %s',
#         '%s %s ((%s %s %s) %s %s)',
#         '%s %s (%s %s (%s %s %s))')
'''
import itertools, random

numlist = [random.randint(1, 13) for i in range(4)]  # 随机4个数
print(numlist)
#permutations(iterable [,r]):
#创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同：
nlist = []
[nlist.append(nl) for nl in list(itertools.permutations(numlist)) if nl not in nlist]  #4个数排列组合,并在有重复数字时对组合去重
#print(nlist)
#product(iter1, iter2, ... iterN, [repeat=1]):
#创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数。
option = ['+', '-', '*', '/']
olist = list(itertools.product(option, repeat=3))  # 操作符重复组合3位
#print(olist)
#拼凑4个数和3个操作符
retlist = ["(" + "(" +str(nl[0]) + ol[0] + str(nl[1]) + ")" + ol[1] + str(nl[2]) + ")" + ol[2] + str(nl[3])
           for nl in nlist for ol in olist]
retlist1 = ["(" + str(nl[0]) + ol[0] + str(nl[1]) + ")" + ol[1] + "(" + str(nl[2]) + ol[2] + str(nl[3]) + ")"
           for nl in nlist for ol in olist]
retlist2 = ["(" + str(nl[0]) + ol[0] + "(" + str(nl[1])+ ol[1] + str(nl[2]) + ")" + ")" + ol[2] + str(nl[3])
           for nl in nlist for ol in olist]
retlist3 = [str(nl[0]) + ol[0] + "(" + "(" + str(nl[1])+ ol[1] + str(nl[2]) + ")" + ol[2] + str(nl[3]) + ")"
           for nl in nlist for ol in olist]
retlist4 = [str(nl[0]) + ol[0] + "(" + str(nl[1])+ ol[1] + "(" + str(nl[2]) + ol[2] + str(nl[3]) + ")" + ")"
           for nl in nlist for ol in olist]
#print(retlist)
retlists = [retlist, retlist1, retlist2, retlist3, retlist4]
#设置一个bool变量，用来记录随机的这4个数是否可以通过四则运算得到24点
count = False
for ret in retlists:
    for rl in ret:
        try:
            if eval(rl) == 24:
                #当出现了至少一种方法得到24点的时候，将bool变量置为真
                count = True
                print(rl + '=24')
        except:
            pass
if count == False:
    print("This not the result I want!")
