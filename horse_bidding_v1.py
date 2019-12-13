#horse_bidding_v1.py
#小型赌马游戏雏形
from HorseGameSetting import *
from time import sleep

#赌马者设置：进入游戏，赌马者初始化
game_opening()
player_name = input('给自己起一个好听的名字叭:\n')
player = player_setting(player_name)

#游戏规则说明
sleep(1.5)
game_rule()

#进入游戏
state = 'go'
while state != 'finish':
    #马场初始化
    horse_pink = 0
    horse_stake = 0
    horse_names = horse_used()
    horse_times = {}
    print('本局比赛参赛的马有：')
    for horse_id, horse_name in horse_names.items():
        print(horse_id, horse_name, sep=": ")
        sleep(0.5)
    print()

    #玩家下注
    try:
        while horse_pink not in horse_names.keys():
            horse_pink = int(input('请选择您下注的马(序号): \n'))
        print('您下注的马是：{}\n'.format(horse_names[horse_pink]))
        while not (100 <= horse_stake <= player['money']):
            horse_stake = eval(input('请输入您的下注金额(最低100):\n'))
        print('您下注的金额是: {}元'.format(horse_stake))
        player['money'] -= horse_stake
        sleep(1)
    except:
        print('输入有误!')
        continue

    #赌马实战
    print('\n{0:-^50}'.format('赌马开始！'))
    for name in horse_names.values():
        horse_times[name] = one_horse(name)
    print()
    
    #结果处理,赌资计算,称号更新
    print('裁判正在紧张处理比赛结果中，请稍后...')
    sleep(2)
    award = result_processing(horse_times,horse_pink,horse_stake,horse_names)
    player['money'] += award
    player['title'] = title_updating(player['money'])
    if player['money'] < 100:
        print('您赌马赌破产了！')
        sleep(1)
        break
    
    #下一局
    state = next_games(player)
else:
    end_of_game(player)
    sleep(1)
