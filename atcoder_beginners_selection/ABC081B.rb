n = gets.to_i
a = gets.chomp.split(" ").map(&:to_i)
ck = true
cnt = 0
while  ck == true do
  i = 0
  n.times do
	if a[i] % 2 == 1 then
		ck = false
	else
		a[i] = a[i] / 2
		i += 1
	end
  end
  cnt += 1 if ck == true
end

print cnt