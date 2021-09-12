import numpy as np

deck = []
for i in range(3, 16):
    deck.extend([i for _ in range(4)])
deck.extend([16, 17])

EnvToReal = {
    3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K',
    14: 'A', 15: '2', 16: 'X', 17: 'D'
}

RealToEnv = {
    '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14, '2': 15, 'X': 16, 'D': 17
}

def generate():
    """
    :return: 获取一副新牌
    """
    d = deck.copy();
    np.random.shuffle(d)
    card_play_date = {
        'landlord' : d[:20],
        'landlord_up' : d[20 : 37],
        'landlord_down' : d[37:54],
        'three_card' : d[17:20]
    }
    for key in card_play_date:
        card_play_date[key].sort()
    return card_play_date


if __name__ == '__main__':
    print(generate())