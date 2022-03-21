""" 
１行にスペース区切りで入力された整数のリスト化
入力 2 4 5 6
出力 [2,4,5,6]
 """
s = list(map(int, input().split()))

""" 
１行毎に入力された整数のリスト化
入力 
2
4
5
出力 [2,4,5]
 """
s = [int(input()) for i in range(3)]


""" リストから重複した値を削除 """
arr = []
list(set(arr))

""" リストから特定の値の重複した個数を確認 """
arr.count("a")

""" リストから重複した値を抽出 """
dup = [x for x in set(arr) if arr.count(x) > 1]

""" for文でリストのインデックス番号を使用 """
for index, num in enumerate(arr):


""" 配列を文字列に変換 """
arr = ['a','b','c']
print("".join(arr))
""" 出力: abc """



