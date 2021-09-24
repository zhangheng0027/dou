import os
import pickle
from typing import List

from collections import Counter

type_error = 0x0  # 非法
type_one = 0x1000  # 单张
type_two = 0x2000  # 一对
type_three = 0x3000  # 三不带

type_one_continuity_five = 0x4000  # 五单连
type_one_continuity_six = 0x5000  # 六单连
type_one_continuity_seven = 0x6000  # 7 单
type_one_continuity_eight = 0x7000  # 8 单
type_one_continuity_nine = 0x8000  # 9 单
type_one_continuity_ten = 0x9000  # 10 单
type_one_continuity_eleven = 0xA000  # 11 单
type_one_continuity_twelve = 0xB000  # 12 单

type_two_continuity_three = 0xC000  # 3 双
type_two_continuity_four = 0xD000  # 4 双
type_two_continuity_five = 0xE000  # 5 双
type_two_continuity_six = 0xF000  # 6 双
type_two_continuity_seven = 0x10000  # 7 双
type_two_continuity_eight = 0x11000  # 8 双
type_two_continuity_nine = 0x12000  # 9 双
type_two_continuity_ten = 0x13000  # 10 双  不会有这么好的运气吧

type_three_continuity_two = 0x14000
type_three_continuity_three = 0x15000
type_three_continuity_four = 0x16000
type_three_continuity_five = 0x17000
type_three_continuity_six = 0x18000

type_three_with_one = 0x19000
type_three_with_two = 0x1A000

type_three_continuity_two_with_one = 0x1B000  # 飞机 带 1  8
type_three_continuity_three_with_one = 0x1C000  # 飞机 带 1  12
type_three_continuity_four_with_one = 0x1D000  # 飞机 带 1  16
type_three_continuity_five_with_one = 0x1E000  # 飞机 带 1  20

type_three_continuity_two_with_two = 0x1F000  # 飞机 带 2 10
type_three_continuity_three_with_two = 0x20000  # 飞机 带 2 15
type_three_continuity_four_with_two = 0x21000  # 飞机 带 2 20

type_four_with_two = 0x22000  # 4 带 2 6
type_four_with_two_pair = 0x23000  # 4 带 2 对  8

type_boom = 0x24000

TypeMap = {
    0x0: 'type_error', 0x1000: 'type_one',
    0x2000: 'type_two', 0x3000: 'type_three', 0x4000: 'type_one_continuity_five',
    0x5000: 'type_one_continuity_six', 0x6000: 'type_one_continuity_seven',
    0x7000: 'type_one_continuity_eight', 0x8000: 'type_one_continuity_nine',
    0x9000: 'type_one_continuity_ten', 0xA000: 'type_one_continuity_eleven',
    0xB000: 'type_one_continuity_twelve', 0xC000: 'type_two_continuity_three',
    0xD000: 'type_two_continuity_four', 0xE000: 'type_two_continuity_five',
    0xF000: 'type_two_continuity_six', 0x10000: 'type_two_continuity_seven',
    0x11000: 'type_two_continuity_eight', 0x12000: 'type_two_continuity_nine',
    0x13000: 'type_two_continuity_ten', 0x14000: 'type_three_continuity_two',
    0x15000: 'type_three_continuity_three', 0x16000: 'type_three_continuity_four',
    0x17000: 'type_three_continuity_five', 0x18000: 'type_three_continuity_six',
    0x19000: 'type_three_with_one', 0x1A000: 'type_three_with_two',
    0x1B000: 'type_three_continuity_two_with_one', 0x1C000: 'type_three_continuity_three_with_one',
    0x1D000: 'type_three_continuity_four_with_one', 0x1E000: 'type_three_continuity_five_with_one',
    0x1F000: 'type_three_continuity_two_with_two', 0x20000: 'type_three_continuity_three_with_two',
    0x21000: 'type_three_continuity_four_with_two', 0x22000: 'type_four_with_two',
    0x23000: 'type_four_with_two_pair', 0x24000: 'type_boom'
}


def encode(a):
    b = a & 0xFF000
    if TypeMap.__contains__(b):
        return TypeMap[b], a & 0xFFF
    return "type_error", 0


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
        return type_error
    aa = Counter(cs).most_common(10)
    if 4 == length:
        # 三带一的情况
        (ma, cou) = aa[0]
        if 3 == cou:
            return ma + type_three_with_one
        return type_error

    if 5 == length:
        # 3 带 2
        (ma, cou) = aa[0]
        if 3 == cou:
            return ma + type_three_with_two
        return type_error

    if 6 == length:
        # 4 带二张
        (ma, cou) = aa[0]
        if 4 == cou:
            return ma + type_four_with_two
        return type_error

    if 8 == length:
        (a, b) = aa[0]
        if 4 == b:
            # 4 带 2 对
            if len(aa) == 3 and aa[1][1] == 2 and aa[2][1] == 2:
                return a + type_four_with_two_pair
            return type_error
        else:
            # 飞机
            if len(aa) > 2 and b == aa[1][1] == 3 and aa[1][0] == a + 1:
                return a + 1 + type_three_continuity_two_with_one
            return type_error

    if 10 == length:
        if len(aa) == 4 and 3 == aa[0][1] == aa[1][1] and aa[1][0] == aa[0][0] + 1 \
                and aa[2][1] == aa[3][1]:
            return aa[1][0] + type_three_continuity_two_with_two
        return type_error

    if 12 == length:
        # 3 飞 带 1
        if len(aa) > 3 and 3 == aa[0][1] == aa[2][1] and aa[0][0] + 2 == aa[2][0]:
            return aa[2][0] + type_three_continuity_three_with_one
        return type_error

    if 15 == length:
        # 3 飞 带 2
        if len(aa) == 6 and 3 == aa[0][1] == aa[2][1] and aa[0][0] + 2 == aa[2][0]\
                and 2 == aa[5][1]:
            return aa[2][0] + type_three_continuity_three_with_two
        return type_error

    if 16 == length:
        # 4 飞 带 1
        if len(aa) > 4 and 3 == aa[0][1] == aa[3][1] \
                and aa[0][0] + 3 == aa[3][0]:
            return aa[3][0] + type_three_continuity_four_with_one
        return type_error

    if 20 == length:
        if len(aa) == 8 and 3 == aa[0][1] == aa[3][1] and aa[0][0] + 3 == aa[3][0] \
                and 2 == aa[4][1] == aa[7][1]:
            return aa[3][0] + type_three_continuity_four_with_two
        else:
            if len(aa) > 5 and 3 == aa[0][1] == aa[4][1] and aa[0][0] + 4 == aa[4][0]:
                return aa[4][0] + type_three_continuity_five_with_one

    return type_error


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
    cou = type_one_continuity_five
    for i in range(5, 15):
        for j in range(3, 16 - i):
            ll = ''.join(['%s' % z for z in range(j, i + j)])
            t[ll] = cou + i + j - 1
        cou = cou + 0x1000


def generateCardType_two(t: {}):
    """
    生成双连
    :param t:
    :return:
    """
    cou = type_two_continuity_three
    for i in range(3, 11):
        for j in range(3, 16 - i):
            ll = ''.join(['%s%s' % (z, z) for z in range(j, i + j)])
            t[ll] = cou + i + j - 1
        cou += 0x1000


def generateCardType_three(t: {}):
    """
    生成飞机
    :param t:
    :return:
    """
    cou = type_three_continuity_two
    for i in range(2, 7):
        for j in range(3, 16 - i):
            ll = ''.join(['%s%s%s' % (z, z, z) for z in range(j, i + j)])
            t[ll] = cou + i + j - 1
        cou += 0x1000


def generateCardType_other(t: {}):
    for i in range(3, 18):
        t[str(i)] = type_one + i

    for i in range(3, 16):
        t[str(i) * 2] = type_two + i
        t[str(i) * 3] = type_three + i
        t[str(i) * 4] = type_boom + i

    t['1617'] = type_boom + 17


if __name__ == '__main__':
    aa = selectCardType([3,4,5,6,7,8,9])
    print(encode(aa))
