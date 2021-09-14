from env import cardType

if __name__ == '__main__':
    m = [3, 3, 4, 4, 4, 3, 5, 6]
    # generateCardType_three(m)
    # a = Counter(m).most_common(5)
    print(cardType.encode(cardType.selectCardType(m)))
