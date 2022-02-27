n,a,b = map(int, input().split())
num = 0
total = 0
for i in range(1,n+1):
    num = list(map(str,str(i)))
    num = [int(i) for i in num]
    num = sum(num)
    if num>=a and num<=b:
      total += i
print(total)
