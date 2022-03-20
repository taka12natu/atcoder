s = list(input().split())
t = list(input().split())
cnt = 0
for index,letter in enumerate(s):
  if not letter == t[index]:
    pos = t.index(letter)
    t[pos] = t[index]
    t[index] = letter
    cnt += 1
if cnt%2 == 0:
  print('Yes')
else:
  print('No')