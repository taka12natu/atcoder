n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in b:
  if a.count(i)==0:
    print("No")
    exit()
  elif a.count(i)<b.count(i):
    print("No")
    exit()
print("Yes")
