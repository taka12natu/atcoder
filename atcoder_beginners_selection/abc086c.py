""" 
・tが奇数の時、x+yは奇数でなければならず、その逆も然り
・t < x+y は成立しない
2回目以降の移動の際には条件がどう変わるか
・t-(pre-t)< x+y-(pre(x+y))
※１つ前の時点との差で考える
※偶数、奇数の条件は不変

１行ずつ判定
 """

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
print(arr)