n,k,x=map(int,input().split())
A=list(map(int, input().split()))
for i,a in enumerate(A):
  if a>x and k>0:
    c = a//x
    if k>=c:  
      A[i] = a - x*c
      k -= c
    else:
      A[i]=a-x*k
      k = 0
      break
if k>0:
  A.sort(reverse=True)
  if k<=len(A):
    for i in range(k):
      A[i] = 0
  else:
    print(0)
    exit()
print(sum(A))