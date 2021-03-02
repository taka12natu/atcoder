n,total = gets.chomp.split(" ").map(&:to_i)
input = "-1 -1 -1"
sum_x = 0
(n+1).times do |x|
  sum_x = 10000 * x
  	  sum_y = 0
	(n-x+1).times do |y|
	  sum_y = 5000 * y
	  sum_z = 0
	    (n-x-y+1).times do |z|
	      sum_z = 1000 * z
	      if total == sum_x + sum_y + sum_z then
	  		input = "#{x} #{y} #{z}"
	  	  end
	  	end
	end
end
p input