for i in range(5, 101):
    if i %7 == 0 and not i %5 == 0:
        print(i, end=',')
