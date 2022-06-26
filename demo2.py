file = open('E:/Desktop/bit.txt', 'r')

for i in file:
    for j in range(0, 9):
        print(i[j], end='\t')
    # print("")
    # x = i[0:9]
    a = i[9:12]
    print(a, end='\t')
    b = i[12:15]
    print(b, end='\t')
    c = i[15:18]
    print(c, end='\t')
    for j in range(18,24):
        print(i[j],end='\t')
    print("")
    # u = i[18:24]
    # print("{}\t{}\t{}\t{}\t{}".format(x,a,b,c,u))

# for i in range(0,61):
#     print("%02x" % i)
