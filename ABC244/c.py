n = int(input())
max_num = 2*n+1
arr = [0 for x in range(max_num)]
flg = True
while flg:
  for i,j in enumerate(arr):
    if j == 0:
      print(i+1, flush=True)
      arr[i] = 1
      break
  n_ans = int(input())
  if n_ans == 0:
    exit()
  else:
    arr[n_ans-1] = 1
