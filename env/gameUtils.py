from typing import List


def selectCount(cs: List):
    # cs.sort()
    arr = [0 for _ in range(15)]
    for i in cs:
        arr[i - 3] += 1

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
        for i in range(13):
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

    l4 = []
    l3 = []
    l2 = []
    l1 = []



    return arr


if __name__ == '__main__':
    m = [3, 3, 4, 4, 4, 3, 5, 6, 4, 5, 7, 8, 9, 10]
    # generateCardType_three(m)
    # a = Counter(m).most_common(5)
    print(selectCount(m))
