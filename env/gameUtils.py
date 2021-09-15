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

    def recovery(ar: [], index, cou, de):
        for i in range(index - cou + 1, index + 1):
            ar[i] += de

    def oneCount(ar: []):
        index, cou = selectOne(ar)
        if index < 0:
            c = 0
            for v in ar:
                if v > 0:
                    c += 1
            return c
        c = oneCount(ar)
        if c <= 1:
            recovery(ar, index, cou, 1)
            return c + 1
        for _ in range(0, cou - 5):
            ar[index] += 1
            index -= 1
            c = min(c, oneCount(ar))
        recovery(ar, index, 5, 1)
        return c + 1

    def countTwo(ar: [], minC = 53):
        index, cou = selectTwo(ar)
        if index < 0:
            return oneCount(ar)
        if minC <= 0:
            recovery(ar, index, cou, 2)
            return 53

        d = min(minC, oneCount(ar))
        d = min(d, countTwo(ar, d - 1))

        for _ in range(0, cou - 3):
            ar[index] += 2
            index -= 1
            d = min(d, oneCount(ar))
            d = min(d, countTwo(ar, d - 1))
        recovery(ar, index, 3, 2)
        return d
    return countTwo(arr, oneCount(arr))


if __name__ == '__main__':
    m = [3,4,5,6,7,8,9,10,11,12,13,14,10,11,7,8,9]
    m.sort()
    print(m)
    # generateCardType_three(m)
    # a = Counter(m).most_common(5)
    print(selectCount(m))
