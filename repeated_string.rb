#!/bin/ruby

# Lilah has a string, s, of lowercase English letters that
# she repeated infinitely many times.

# Given an integer, n, find and print the number of letter a's
# in the first n letters of Lilah's infinite string.

# For example, if the string s = 'abcac' and n = 10, the
# substring we consider is abcacabcac, the first 10 characters
# of her infinite string. There are 4 occurrences of a in the
# substring.

# Complete the repeatedString function below. It should return
# an integer representing the number of occurrences of a in the
# prefix of length n in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider

def repeatedString(s, n)
  newS = s.split('')
  s_length = newS.length
  #find number of a's in s
  as = newS.count('a')
  #find how many s can we fit in n
  times = n / s_length
  #find the remainder
  remainder = n % s_length

  #find total number of a's
  total_a = as * times + newS.slice(0, remainder).count('a')
end

puts repeatedString('aba', 10)
puts repeatedString('a', 10000000000000)
