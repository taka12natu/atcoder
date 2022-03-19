n = int(input())
a = int(input())
output = []
for i in range(n-1):
  next = int(input())
  if next == a:
    output.append('stay')
  elif next < a:
    output.append('down ' + str(abs(next-a)))
  elif next > a:
    output.append('up '+ str(abs(next-a)))
  a = next
for result in output:
  print(result)