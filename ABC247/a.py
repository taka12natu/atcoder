from ntpath import join
s = list(input())
s[3] = s[2]
s[2] = s[1]
s[1] = s[0]
s[0] = "0"
print("".join(s))