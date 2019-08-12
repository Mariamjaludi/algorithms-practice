def palindrome_num n
  divisor = 1
  while n / divisor >= 10
    divisor *= 10
  end
  while n != 0
    first = n / divisor;
    last = n % 10
    return false if first != last

    n = (n % divisor) / 10
    divisor /= 100
  end
  true
end



 # n = [101, 100, 20202, 111, 112]

 m = 3002

 puts palindrome_num(m)


 # n.each {|n| puts palindrome_num(n)}s
