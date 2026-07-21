list_nums = input().split()
int_lst = list(map(int,list_nums))
answer = 0
for i in range(1, len(int_lst) - 1):
    L = int_lst[i]
    for j in range(i):
        L = max(L, int_lst[j])
    R = int_lst[i]
    for k in range(i + 1, len(int_lst)):
        R = max(R, int_lst[k])
    answer += (min(L, R) - int_lst[i])
print(answer)