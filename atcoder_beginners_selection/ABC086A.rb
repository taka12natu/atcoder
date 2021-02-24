a,b = gets.chomp.split(" ").map(&:to_i)

cal = a * b

if cal % 2 == 0 then
	print "Even"
else
	print "Odd"
end