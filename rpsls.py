#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：土木3班蒋旭杰
日期：2021/12/1
"""

import random
comp_number=random.randint(0,4)


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name==("石头"):
        number=str(o)
        return number
    if name==("史波克"):
        number=str(1)
        return number
    if name==("纸"):
        number=str(2)
        return number
    if name==("蜥蜴"):
        number=str(3)
        return number
    if name==("剪刀"):
        number=str(4)
        return number

    pass #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==(0):
        name=str("石头")
        return namen
    if number==(1):
        name=str("史波克")
        return name
    if number==(2):
        name=str("纸")
        return name
    if number==(3):
        name=str("蜥蜴")
        return name
    if number==(4):
        name=str("剪刀")
        return name


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    if player_choice==(0) and (comp_numbere==(4) or comp_number==(3)):
        print("你赢了")
    elif player_choice==(1) and (comp_number==(0) or comp_number==(4)):
        print("你赢了")
    elif player_choice == (2) and (comp_number == (0) or ccomp_number==(1)):
        print("你赢了")
    elif player_choice == (3) and (comp_number == (1) or comp_number==(3)):
        print("你赢了")
    elif player_choice == (4) and (comp_number==(2) or comp_number==(3)):
        print("你赢了")
    elif player_choice == (0) and comp_number==(0):
        print("平局")
    elif player_choice == (1) and comp_number==(1):
        print("平局")
    elif player_choice == (2) and comp_number==(2):
        print("平局")
    elif player_choice == (3) and comp_number==(3):
        print("平局")
    elif player_choice == (4) and comp_number==(4):
        print("平局")
    else:
        print("机械赢了")
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    pass #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("---------")
print("请输入您的选择:")
choice_name=input()
print("计算机的选择为"+str(number_to_name(comp_number)))
rpsls(choice_name)


