n = int(input())

while n >= 26:
    n -= 26
while n <= -26:
    n += 26

string = input()
string = string.lower()
lst = []
count = 0
ls = list(string)

for z in range(len(ls)):
    i = ls[z]
    if i == ' ':
        count += 1
        lst.append(i)
    else:
        parameter = ord(i) + n + z - count
        while parameter > ord('z'):
            parameter -= 26
        while parameter < ord('a'):
            parameter += 26
        lst.append(chr(parameter))

print(''.join(lst))