#HorseGameSetting
#跑马游戏自编库函数
#JamesBourbon
def one_horse(name):
    #利用进度条函数完成跑马
    import time,random#,math
    gap = random.randint(100,500)/10000
    #gap = math.sin(int(time.perf_counter())%10)/10+random.randint(1500,2500)/10000
    #利用sleep(gap)控制马的能力，gap可以是一个随时间变化的量
    scale = 50
    start = time.perf_counter()
    for i in range(scale+1):
        a = '-' * i
        b = '.' * (scale-i)
        c = (i/scale)*100
        dur = time.perf_counter() - start
        #name = "{:^14}".format(name)
        name = f'{name:^15}'
        bar = "\r{} {:3.0f}%[{}<🐴|{}]{:.2f}s".format(name,c,b,a,dur)
        print(bar,end="")
        time.sleep(gap)
    print('\n',end='')
    return dur


def player_setting(name):
    #玩家信息初始化与交互信息
    player = {
        'name':name,
        'money':3000,
        'title':'新手赌马师'
    }
    message = '{}加入了游戏！初始资金为{}元！您现在是{}'
    message = message.format(player['name'],player['money'],player['title'])
    print(message)
    return player


def horse_used():
    import random
    #从马场已有马中随机抽取参赌马匹
    name_list = ['贝克街的亡灵','漆黑的追踪者','侦探们的镇魂歌',
            '纯黑的噩梦','业火的向日葵','绀青之拳',
            '绝海的侦探','第十一个前锋','世纪末的魔术师',
            '唐红的恋歌','异次元的狙击手','银翼的奇术师',]
    horses = {}
    horse_count = 8
    for i in range(horse_count):
        horse = (random.choice(name_list))
        name_list.remove(horse)
        horses[i+1] = horse
    return horses 


def game_opening():
    from time import sleep
    #初始介绍信息
    message = '''
-------------赌马游戏V1.0测试版------------
-------------------------> by JamesBourbon
-----在本游戏中您将体验到毛利小五郎的喜怒哀乐-----
----你将成为一个赌马爱好者，加入到这场马的盛宴！----
'''
    print(message)
    sleep(3)
    

def game_rule():
    #游戏规则说明
    from time import sleep
    message = '''
-----------------游戏规则----------------
每局赌马开始后，您将在各马之间选择一匹最有潜力的马下注
下注时您需要付出一定的金钱
如果您下注的马跑进了前三，您会获得基于您所下赌资的奖励！
还等什么，让我们开始游戏吧！
'''
    print(message)
    sleep(3)


def result_processing(horse_times,horse_pink,horse_stake,horse_names):
    from time import sleep
    results = list(horse_times.items())
    results.sort(key=lambda x:x[1])
    #将字典键值对处理成元组列表，再从小到大排序
    print('{:-^50}'.format('胜负已分！'))
    count = 0
    #名次公布
    for result,mark in results:
        count += 1
        print('第{}名：{}! 所用时间:{:.2f}s'.format(count,result,mark))
    #颁奖
    print()
    sleep(1)
    if horse_names[horse_pink] == results[0][0]:
        print('你赌的马在本次比赛中荣获冠军！')
        award = horse_stake*20+1500
    elif horse_names[horse_pink] == results[1][0]:
        print('你赌的马在本次比赛中获得亚军！')
        award = horse_stake*10+1000
    elif horse_names[horse_pink] == results[2][0]:
        print('你赌的马在本次比赛中获得季军！')
        award = horse_stake*5+500
    else:
        print('你赌的马在本次比赛中表现不突出！再接再厉！')
        return 0
    sleep(1)
    print('您获得奖金{}元！'.format(award))
    return award


def next_games(player):
    from time import sleep
    ind = ' '
    while True:
        message = '''
是否开始下一局游戏？
输入finish，您便可以立即带着赌资离场，并保留现有称号
输入go，您将开始下一局赌马
输入check，您可以查看您的玩家状态
其他输入将回到该提示输入状态：
'''
        ind = input(message)
        if ind == 'check':
            player_message = '''
赌马师你好！您的信息如下：
您的名字是: {}, 您现在是: {}, 您现有赌资为: {}'''
            player_message = player_message.format(
                player['name'],player['title'],player['money'])
            print(player_message)
            sleep(2)
        elif ind == 'finish':
            return ind
        elif ind == 'go':
            print('下一局赌马开始！\n')
            sleep(1)
            return ind
        else:
            pass 


def title_updating(player_money):
    #赌马师等级实时更新
    title = ''
    if 3500 < player_money < 6000:
        title = '初级赌马师'
    elif 6000 <= player_money < 12000:
        title = '中级赌马师'
    elif 12000 <= player_money < 20000:
        title = '高级赌马师'
    elif 20000 <= player_money < 30000:
        title = '赌马大师'
    elif player_money >= 30000:
        title = '荣誉赌马大师'
    else:
        title = '新手赌马师'
    print('您现在的称号是: {}'.format(title))
    return title


def end_of_game(player):
    message = '''
游戏结束！您的游戏记录如下:
您的名字: {}
您的剩余赌资为: {}元
您的称号是: {}
感谢您的参与！
'''.format(player['name'],player['money'],player['title'])
    print(message)
