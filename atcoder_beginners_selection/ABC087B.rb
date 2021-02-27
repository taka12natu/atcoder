a = gets.to_i
b = gets.to_i
c = gets.to_i
x = gets.to_i
cnt = 0
i = 1
for a_i in 0..a do
	cal_a = 500 * a_i
	for b_i in 0..b do
	 	cal_b = 100 * b_i
		for c_i in 0..c do
			cal_c = 50 * c_i
			if cal_a + cal_b + cal_c == x then
				cnt += 1
			end
		end
	end
end

print cnt
