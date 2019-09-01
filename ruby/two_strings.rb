#!/bin/ruby
# frozen_string_literal: true

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring.
# Function Description

# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

# twoStrings has the following parameter(s):

# # s1, s2: two strings to analyze .
def twoStrings(s1, s2)
  s1_array = s1.split('')
  answer = 'NO'
  s1_array.each do |letter|
    if s2.include? letter
      answer = 'YES'
      return answer
    end
  end
  answer
end

puts twoStrings('hello', 'world')
puts twoStrings('hi', 'world')
