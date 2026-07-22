s = input()
n = int(input())
word = input()
lstt = list(s)
listt = ''
cnt = 0
letter = 0

for i in range(len(lstt)):
    if lstt[i] != ' ':
        letter += 1
        if letter == n:
            index = i
            break

new = ord(lstt[index]) - ord(word)

for z in range(len(lstt)):
    i = lstt[z]
    if i == ' ':
        cnt += 1
        listt += i
    else:
        order = ord(i) - z - new + cnt
        while order < ord('a'):
            order += 26
        while order > ord('z'):
            order -= 26
        listt += chr(order)

print(listt)