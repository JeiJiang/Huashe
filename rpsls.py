#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ľ3�཯���
���ڣ�2021/12/1
"""

import random
comp_number=random.randint(0,4)


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name==("ʯͷ"):
        number=str(o)
        return number
    if name==("ʷ����"):
        number=str(1)
        return number
    if name==("ֽ"):
        number=str(2)
        return number
    if name==("����"):
        number=str(3)
        return number
    if name==("����"):
        number=str(4)
        return number

    pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==(0):
        name=str("ʯͷ")
        return namen
    if number==(1):
        name=str("ʷ����")
        return name
    if number==(2):
        name=str("ֽ")
        return name
    if number==(3):
        name=str("����")
        return name
    if number==(4):
        name=str("����")
        return name


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if player_choice==(0) and (comp_numbere==(4) or comp_number==(3)):
        print("��Ӯ��")
    elif player_choice==(1) and (comp_number==(0) or comp_number==(4)):
        print("��Ӯ��")
    elif player_choice == (2) and (comp_number == (0) or ccomp_number==(1)):
        print("��Ӯ��")
    elif player_choice == (3) and (comp_number == (1) or comp_number==(3)):
        print("��Ӯ��")
    elif player_choice == (4) and (comp_number==(2) or comp_number==(3)):
        print("��Ӯ��")
    elif player_choice == (0) and comp_number==(0):
        print("ƽ��")
    elif player_choice == (1) and comp_number==(1):
        print("ƽ��")
    elif player_choice == (2) and comp_number==(2):
        print("ƽ��")
    elif player_choice == (3) and comp_number==(3):
        print("ƽ��")
    elif player_choice == (4) and comp_number==(4):
        print("ƽ��")
    else:
        print("��еӮ��")
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("---------")
print("����������ѡ��:")
choice_name=input()
print("�������ѡ��Ϊ"+str(number_to_name(comp_number)))
rpsls(choice_name)


