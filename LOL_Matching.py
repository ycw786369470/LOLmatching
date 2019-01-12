# LOL匹配系统模拟
# 规则
# 同一大段位只能匹配到相同大段位的玩家 青铜白银黄金就是大段位，青铜几、白银几是小段位
# 比如青铜1可以匹配青铜1~5段位的玩家，而不能匹配到高于自己段位的玩家，如青铜无法匹配到白银或黄金段位
# 可优化：不完全限制在同一段位里，可以匹配到小段位小于3的玩家，比如白银1可以匹配到最大黄金3段位的玩家，最小匹配到白银4的玩家
# （待改进）
# Time:11/30 15:52

import time
import random

class NewUser(object):#新建一个用户
    def __init__(self):
        pass


    def new_player(self):

        #玩家生成名字++self.player_name
        word_list = ['水', '天','光', '神',]
        self.player_name = str(word_list[random.randint(0,3)]+word_list[random.randint(0,3)]+word_list[random.randint(0,3)]+word_list[random.randint(0,3)])+str(random.randint(1,20))

        #玩家生成段位代码++self._rank  名字self._rankname
        self._rankname = '' #段位名称
        #创建玩家的大段位(青铜-白银-黄金-铂金-钻石-王者)
        self._rank = random.randint(0,5)
        if self._rank == 0:
            self._rankname = '欠揍青铜'
        elif self._rank == 1:
            self._rankname = '辣鸡白银'
        elif self._rank == 2:
            self._rankname = '挖煤黄金'
        elif self._rank == 3:
            self._rankname = '废物铂金'
        elif self._rank == 4:
            self._rankname = '摧残钻石'
        elif self._rank == 5:
            self._rankname = '嘴强王者'

        #创建玩家的小段位（1-5）
        self._rank_num = random.randint(1,6)

        #返回*****
        return self.player_name,self._rank,self._rank_num,self._rankname

    def get_rank(self):
        pass

    # 显示信息
    def __str__(self):
         return '玩家【%s】加入游戏,它的段位是：%s--%s'%(str(self.player_name),str(self._rankname),str(self._rank_num))


class Matching(object):
    def __init__(self):
        pass

    def f_player(self,player,big_rank,small_rank,rn): # 生成第一个进入匹配队列的玩家
        self.p1 = player
        self.b1 = big_rank
        self.s1 = small_rank
        self.group = []
        self.group.append(self.p1) #在group内添加玩家
        print('第一个加入的玩家段位为：',rn)

    def rank_get(self,player,big_rank,small_rank): #从NewUser返回值中获得玩家名字player大段位bigrank和小段位smallrank信息
        #已加入队列的玩家
        # self.player1_b = big_rank
        # self.player1_s = small_rank
        time.sleep(1)
        print('检验该玩家是否符合段位要求')
        time.sleep(1)
        print('判断中...')
        time.sleep(1)
        if big_rank == self.b1 or self.b1-1 <= big_rank <= self.b1+1 > self.b1-1 :
            self.group.append(player)
            print(player,'成功加入匹配队列')
        else:
            print('该玩家段位不符合，继续匹配')
            print()
            print()
            print()
        print('队列内的玩家有：',self.group)
        print()
        print()
        print()


        #########################
        #测试接收状况
        # print('接收到的玩家名字:',player)
        # print('接收到的玩家大段位:',big_rank)
        # print('接收到玩家的小段位',small_rank)
        ###########################



    def print_group(self):
        print('打印小组内已匹配的人数')


new = NewUser()
mat = Matching()

def main1():#测试生成玩家
    new.new_player()
    print(new)
# main1()

def main2():#测试接收玩家信息
    # 创建初始加入group的玩家
    p1,b1,s1,rn = new.new_player()
    mat.f_player(p1,b1,s1,rn)
    while 1 :
        #循环：不断的生成玩家
        p,b,s,rn = new.new_player() # 生成玩家
        print(new) #打印出生成玩家的情况
        mat.rank_get(p,b,s) #将生成玩家的名字、大小段位传入函数Matching中并判断是否满足条件
        print('匹配中.')
        time.sleep(1)
        print('匹配中..')
        time.sleep(1)
        print('匹配中...')
        time.sleep(1)
        print('匹配成功')
main2()














