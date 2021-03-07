n,l = gets.chomp.split(" ").map(&:to_i)
arr = []
n.times do
	arr << gets.chomp
end
arr_sort = arr.sort
print arr_sort.join
