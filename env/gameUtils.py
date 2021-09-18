from typing import List

from env import game


def selectCount(cs: List):
    arr = [0 for _ in range(15)]
    for i in cs:
        arr[i - 3] += 1
    count = 0
    if arr[13] == 1 or arr[14] == 1:
        if arr[13] == 1 and arr[14] == 1:
            count -= 1.509  # 对王 相当于多出 1.5 手
        else:
            count += 1
        arr[13] = arr[14] = 0

    if arr[12] > 0:
        arr[12] = 0
        count += 1
    lastIndex = 0
    iss = False
    for index, val in enumerate(arr):
        if iss:
            if val != 0:
                continue
            count += _selectCount(arr[lastIndex:index])
            iss = False
        else:
            if val != 0:
                iss = True
                lastIndex = index
    return count


def _selectCount(arr: List):
    def selectFour(ar: []):
        for i, val in enumerate(ar):
            if val == 4:
                ar[i] = 0
                return i, 1
        return -1, 0

    def selectThree(ar: []):
        cou = 0
        for i, val in enumerate(ar):
            if val >= 3:
                cou += 1
                ar[i] -= 3
            elif cou > 0:
                return i - 1, cou
        return -1, 0

    def selectTwo(ar: []):
        cou = 0
        for i, val in enumerate(ar):
            if val >= 2:
                cou += 1
            elif cou >= 3:
                for j in range(i - cou, i):
                    ar[j] -= 2
                return i - 1, cou
            else:
                cou = 0
        return -1, 0

    def selectOne(ar: []):
        cou = 0
        for i in range(len(ar)):
            if ar[i] >= 1:
                cou += 1
            elif cou >= 5:
                for j in range(i - cou, i):
                    ar[j] -= 1
                return i - 1, cou
            else:
                cou = 0
        if cou >= 5:
            for j in range(i - cou, i):
                ar[j] -= 1
            return i - 1, cou
        return -1, 0

    def recovery(ar: [], index, cou, de):
        for i in range(index - cou + 1, index + 1):
            ar[i] += de

    def oneCount(ar: [], mc=54):
        index, cou = selectOne(ar)
        if index < 0:
            c = 0
            for v in ar:
                if v > 0:
                    c += 1
            return c
        # c = oneCount(ar)
        # if c <= 1:
        #     recovery(ar, index, cou, 1)
        #     return c + 1
        rightCount = oneCount(ar[index + 1:])
        f, leftCount = splitCard(ar, oneCount, mc)
        if f:
            leftCount = leftCount - rightCount
        for _ in range(0, cou - 5):
            ar[index] += 1
            index -= 1
            f, cc = splitCard(ar, oneCount, mc)
            if f:
                cc = cc - cc
            leftCount = min(cc, leftCount)
        recovery(ar, index, 5, 1)
        return leftCount + rightCount + 1

    def countTwo(ar: [], minC):
        index, cou = selectTwo(ar)
        if index < 0:
            return oneCount(ar)
        if minC <= 0:
            recovery(ar, index, cou, 2)
            return 53

        # d = min(minC, oneCount(ar))
        # d = min(d, countTwo(ar, d - 1))

        rightCount = countTwo(ar[index + 1:], minC - 1)
        f, leftCount = splitCard(ar, countTwo, minC - 1)
        if f:
            leftCount = leftCount - rightCount

        for _ in range(0, cou - 3):
            ar[index] += 2
            index -= 1
            f, cc = splitCard(ar, countTwo, minC - 1)
            if f:
                cc = cc - rightCount
            leftCount = min(leftCount, cc)

        recovery(ar, index, 3, 2)
        return leftCount + rightCount + 1

    def countThree(ar: [], minC):
        index, cou = selectThree(ar)
        if index < 0:
            return countTwo(ar, minC)
        if minC < 0:
            return 53
        rightCount = countThree(ar[index + 1:], minC - 1)

        f, leftCount = splitCard(ar, countThree, minC - 1)
        leftCount -= 0.49 * cou
        if f:
            leftCount = leftCount - rightCount

        # leftCount = countThree(ar[:index + 1 - cou], minC - 1) - 0.49 * cou  # 3 带一 相当于多出 0.5 手
        for i in range(index + 1 - cou, index):
            ar[i] += 3
            cou -= 1
            # leftCount = min(leftCount, countThree(ar[: i + 1], minC - 1) - 0.49 * cou)
            f, cc = splitCard(ar, countThree, minC - 1) - 0.49 * cou
            cc -= 0.49 * cou
            if f:
                cc = cc - rightCount
            leftCount = min(leftCount, cc)
        ar[index] += 3
        return min(1 + rightCount + leftCount, countTwo(ar, minC))

    def countFour(ar: [], minC):
        index, cou = selectFour(ar)
        if index < 0:
            return countThree(ar, minC)
        if minC < 0:
            return 53
        m = countFour(ar[index + 1:], minC - 1) + countFour(ar[:index], minC - 1) - 1.009  # 4 个相当于多出 1 手
        ar[index] += 4
        return min(m, countThree(ar, minC))

    def splitCard(ar: [], ff, minC):
        for index, val in enumerate(ar):
            if val == 0:
                return False, ff(ar[:index + 1], minC)
        return True, ff(ar, minC)

    return countFour(arr, oneCount(arr))


if __name__ == '__main__':
    # cs = game.generateNewCard()
    # print(cs['landlord'])
    # print(cs['landlord'], selectCount(cs['landlord']))
    # print(cs['landlord_up'], selectCount(cs['landlord_up']))
    # print(cs['landlord_down'], selectCount(cs['landlord_down']))
    a = [8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 12, 13, 13, 14]
    print(selectCount(a))
