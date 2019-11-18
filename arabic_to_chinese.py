#*encoding=utf-8
# constants for arabic_to_chinese
CN_NUM = {
    1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九',0:''
}
CN_UNIT = {
    10:'十',
    100:'百',
    1000:'千',
    10000:'万'
}

def arabic_to_chinese(ara:int) -> str:
    if ara < 10:
        val = CN_NUM[ara]
    if 10 <= ara < 100:
        hv = int(ara/10)
        hv2 = CN_NUM[hv]
        lv = ara%10
        lv2 = CN_NUM[lv]
        if hv == 1:
            val = '十' + lv2
        else:
            val = hv2 + '十' + lv2
    if 100 <= ara < 1000:
        pass
    return val


# TODO: make a full unittest
def test():
    # test_dig = ['1',
    #             '11',
    #             '23',
    #             '56',
    #             '101']
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    for ara in test:
        x = arabic_to_chinese(ara)
        print( x)

if __name__ == '__main__':
    test()
