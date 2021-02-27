n,a,b = gets.chomp.split(" ").map(&:to_i)
sum = 0
for i in 1..n do
	sub_sum = 0
	if i.to_s.length > 1 then
		arr = i.to_s.split("").map(&:to_i)
		arr.each do |num|
			sub_sum += num
		end
	else
		sub_sum += i.to_i
	end
	if sub_sum >= a && sub_sum <= b
		sum += i
	end
end
print sum