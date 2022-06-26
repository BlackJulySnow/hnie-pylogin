file = open('E:/Desktop/1.txt', 'r')


def printbit(x):
    a1 = 0 if (x & 1) == 0 else 1
    a2 = 0 if (x & 2) == 0 else 1
    a3 = 0 if (x & 4) == 0 else 1
    a4 = 0 if (x & 8) == 0 else 1
    print("{}{}{}{}".format(a4, a3, a2, a1), end='')


def get(x):
    x1 = int(x[0], 16)
    x2 = int(x[1], 16)
    printbit(x1)
    print( end='')
    printbit(x2)
    print( end='')


# printbit(1)
for i in file:
    a = i[6:8]
    b = i[4:6]
    c = i[2:4]
    d = i[0:2]
    get(a)
    get(b)
    get(c)
    print("")
    # print(a)
    # a = bin(int(a, 16))
    # b = bin(int(b, 16))
    # c = bin(int(b, 16))
    # print(int(a, 16))
    # print(i)
