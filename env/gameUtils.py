import pickle
from typing import List
import os
from collections import Counter

from env import cardType

t = {}


def selectCardType(cs: List):
    """
    判断牌的类型
    :param cs:
    :return:
    """
    global t
    cs.sort()
    if len(t) == 0:
        if os.path.exists('CardType.tmp'):
            t = pickle.load(open('CardType.tmp', 'rb'))
        else:
            t = generateCardType()
            with open('CardType.tmp', 'wb') as g:
                pickle.dump(t, g)
    st = ''.join(str(i) for i in cs)
    if t.__contains__(st):
        return t[st]

    length = len(cs)
    if length < 4:
        return cardType.type_error
    aa = Counter(cs).most_common(10)
    if 4 == length:
        # 三带一的情况
        (ma, cou) = aa[0]
        if 3 == cou:
            return ma + cardType.type_three_with_one
        return cardType.type_error

    if 5 == length:
        # 3 带 2
        (ma, cou) = aa[0]
        if 3 == cou:
            return ma + cardType.type_three_with_two
        return cardType.type_error

    if 6 == length:
        # 4 带二张
        (ma, cou) = aa[0]
        if 4 == cou:
            return ma + cardType.type_four_with_two
        return cardType.type_error

    if 8 == length:
        (a, b) = aa[0]
        if 4 == b:
            # 4 带 2 对
            if len(aa) == 3 and aa[1][1] == 2 and aa[2][1] == 2:
                return a + cardType.type_four_with_two_pair
            return cardType.type_error
        else:
            # 飞机
            if len(aa) > 2 and b == 3 and aa[1][1] == 3 and aa[1][0] == a + 1:
                return a + cardType.type_three_continuity_two_with_one
            return cardType.type_error

    if 10 == length:
        if len(aa) == 4 and 3 == aa[0][1] == aa[1][1] and aa[1][0] == aa[0][0] + 1 \
                and aa[2][1] == aa[3][1]:
            return aa[0][0] + cardType.type_three_continuity_two_with_two
        return cardType.type_error

    if 12 == length:
        # 3 飞 带 1
        if len(aa) > 3 and 3 == aa[0][1] == aa[2][1] and aa[0][0] + 2 == aa[2][0]:
            return aa[0][0] + cardType.type_three_continuity_three_with_one
        return cardType.type_error

    if 15 == length:
        # 3 飞 带 2
        if len(aa) == 6 and 3 == aa[0][1] == aa[2][1] and aa[0][0] + 2 == aa[2][0]\
                and 2 == aa[5][1]:
            return aa[0][0] + cardType.type_three_continuity_three_with_two
        return cardType.type_error

    if 16 == length:
        # 4 飞 带 1
        if len(aa) > 4 and 3 == aa[0][1] == aa[3][1] \
                and aa[0][0] + 3 == aa[3][0]:
            return aa[0][0] + cardType.type_four_continuity_three_with_one
        return cardType.type_error

    if 20 == length:
        if len(aa) == 8 and 3 == aa[0][1] == aa[3][1] and aa[0][0] + 3 == aa[3][0] \
                and 2 == aa[4][1] == aa[7][1]:
            return aa[0][0] + cardType.type_three_continuity_four_with_two
        else:
            if len(aa) > 5 and 3 == aa[0][1] == aa[4][1] and aa[0][0] + 4 == aa[4][0]:
                return aa[0][0] + cardType.type_three_continuity_five_with_one

    return cardType.type_error


def generateCardType():
    """
    对基础牌进行缓存
    :return:
    """
    temp = {}
    generateCardType_one(temp)
    generateCardType_two(temp)
    generateCardType_other(temp)
    generateCardType_three(temp)
    return temp


def generateCardType_one(t: {}):
    """
    生成单连
    :param t:
    :return:
    """
    cou = cardType.type_one_continuity_five
    for i in range(5, 15):
        for j in range(3, 16 - i):
            ll = ''.join(['%s' % z for z in range(j, i + j)])
            t[ll] = cou + j
        cou = cou + 0x1000


def generateCardType_two(t: {}):
    """
    生成双连
    :param t:
    :return:
    """
    cou = cardType.type_two_continuity_three
    for i in range(3, 11):
        for j in range(3, 16 - i):
            ll = ''.join(['%s%s' % (z, z) for z in range(j, i + j)])
            t[ll] = cou + j
        cou += 0x1000


def generateCardType_three(t: {}):
    """
    生成飞机
    :param t:
    :return:
    """
    cou = cardType.type_three_continuity_two
    for i in range(2, 7):
        for j in range(3, 16 - i):
            ll = ''.join(['%s%s%s' % (z, z, z) for z in range(j, i + j)])
            t[ll] = cou + j
        cou += 0x1000


def generateCardType_other(t: {}):
    for i in range(3, 18):
        t[str(i)] = cardType.type_one + i

    for i in range(3, 16):
        t[str(i) * 2] = cardType.type_two + i
        t[str(i) * 3] = cardType.type_three + i
        t[str(i) * 4] = cardType.type_boom + i

    t['1617'] = cardType.type_boom + 17


if __name__ == '__main__':
    m = [3, 3, 4, 4, 4, 3, 5, 6]
    # generateCardType_three(m)
    # a = Counter(m).most_common(5)
    print(cardType.encode(selectCardType(m)))
