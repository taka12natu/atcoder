n = gets.to_i
arr = gets.chomp.split(" ").map(&:to_i)
a_sum = 0
0.step(n-1,2){|i|
	a_sum += arr.sort.reverse[i]
}
b_sum = 0
1.step(n-1,2){|i|
	b_sum += arr.sort.reverse[i]
}

print a_sum - b_sum