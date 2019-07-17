

# Complete the sockMerchant function below.
def findPairs(ar, find, pairs)
  unless ar.empty?
    newAr = ar
    find_index = newAr.index(find)
    if find_index
      pairs += 1
      newAr = [*newAr.slice(0, find_index), *newAr[(find_index + 1)..-1]]
    end
    return findPairs(newAr.drop(1), newAr[0], pairs)
  end
  pairs
end

def sockMerchant(_n, ar)
  pairs = 0
  find = ar[0]
  findPairs(ar.drop(1), find, pairs)
end

#############################################################
# another way to solve it

def sockMerchant2(_n, ar)
  a = ar.sort
  print a
  puts ''
  b = ar.uniq
  print b
  puts ''
  c = b.map { |sock| a.count(sock) }
  print c
  puts ''
  c.collect! { |sockcount| sockcount / 2 }
  print c
  puts ''
  c.reduce { |sum, pairs| sum + pairs }
end

array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

array2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
m = 10

# puts sockMerchant(n, array)
# puts sockMerchant(m, array2)
# puts 'second method'
puts sockMerchant2(n, array)
# puts sockMerchant2(m, array2)
