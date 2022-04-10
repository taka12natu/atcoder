n = int(input())
arr = []
pre_arr = []
""" 前の列にnを加えて前の列を繰り返すだけ """
for i in range(n):
  arr.append(i+1)
  arr.extend(pre_arr)
  pre_arr = arr.copy()
L=[str(a) for a in arr]
L=" ".join(L)
print(L)

""" 
配列をコピーしたい際に、配列A=配列Bとすると、
配列Aと配列Bは連動してしまい、コピー元のデータが変わると
コピー先のデータも変わってしまう

独立した配列としたい場合にはcopy()を使用する
 """