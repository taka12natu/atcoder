n = int(input())
st = [input().split() for _ in range(n)]
s, t = [list(i) for i in zip(*st)]
t_result=s_result=True
for i in range(n):
  if s.count(s[i]) + t.count(s[i]) > 1 and s[i] != t[i]:
    s_result=False
  if s.count(t[i]) + t.count(t[i]) > 1 and s[i] != t[i]:
    t_result=False
  if s_result==False and t_result==False:
    print("No")
    exit()
print('Yes')