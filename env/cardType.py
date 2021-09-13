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
    b = a & 0xFF000;
    if TypeMap.__contains__(b):
        return TypeMap[b], a & 0xFFF;
    return "type_error", 0


if __name__ == '__main__':
    print(encode(0x10003))
