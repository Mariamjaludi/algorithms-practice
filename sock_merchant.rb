#!/bin/ruby

# iterative solution
array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

array2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
m = 10

def sockMerchant(n, ar)
  a = ar.uniq
  # print a
  b = a.map { |sock| ar.count(sock)}
  # print b
  c = b.collect{ |sockcount| sockcount / 2}
  puts c.inject{|a, b| a + b }
end

puts sockMerchant(n, array)
# puts sockMerchant(m, array2)
