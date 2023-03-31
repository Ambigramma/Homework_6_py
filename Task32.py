lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_n = int(input())
max_n = int(input())
for i in range(len(lst)):
    if min_n <= lst[i] <= max_n:
        print(i)