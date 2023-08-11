n = int(input())

star = ''
for a in range(1,n+1):
    for b in range(0,a):
        star += '*'
    star += '\n'

print(star)