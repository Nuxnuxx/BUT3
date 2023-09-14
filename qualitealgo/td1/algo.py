def algo_1(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            count += 1
    print("Algo 1 schtroumpfer ", count)


def algo_2(n):
    count = 0
    for i in range(n):
        for j in range(1, i+1):
            count += 1
    print("Algo 2 schtroumpfer ", count)


def algo_3(n):
    count = 0
    for i in range(5, n-4):
        print("i", i)
        for j in range(i-5, i+6):
            print("j", j)
            count += 1
    print("Algo 3 schtroumpfer ", count)


def algo_4(n):
    count = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                count += 1
    print("Algo 4 schtroumpfer ", count)


n = 15
algo_1(n)
algo_2(n)
algo_3(n)
algo_4(n)
