require 'pry'
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

find = 0

def binary_search(arr, find)
  min = 0
  max = arr.length - 1
  while max >= min
    guess = ((max + min) / 2).to_i
    # binding.pry
    if find == arr[guess]
      return guess
    end
    if arr[guess] < find
      min = guess + 1
    else
      max = guess - 1
    end
  end
  -1
end

puts binary_search(array, find)
