from typing import List

from env import cardType


def selectCardType(cs: List):
    cs.sort()


def generateCardType():
    """
    生成
    :return:
    """
    t = {}
    generateCardType_one(t)
    generateCardType_two(t)
    generateCardType_other(t)
    return t


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


def generateCardType_other(t: {}):
    for i in range(3, 18):
        t[str(i)] = cardType.type_one + i

    for i in range(3, 16):
        t[str(i) * 2] = cardType.type_two + i
        t[str(i) * 3] = cardType.type_three + i
        t[str(i) * 4] = cardType.type_boom + i

    t['1617'] = cardType.type_boom + 17


if __name__ == '__main__':
    # m = generateCardType()
    print(str(3) * 4)
