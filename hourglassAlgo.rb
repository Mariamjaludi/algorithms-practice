require 'pry'

testArr = [
  [1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0],
  [0, 0, 2, 4, 4, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 0, 1, 2, 4, 0]
]

testArr2 = [
  [1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0],
  [0, 0, 2, 4, 4, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 0, 1, 2, 4, 0]
]

testArr3 = [
  [-1, 1, -1, 0, 0, 0],
  [0, -1, 0, 0, 0, 0],
  [-1, -1, -1, 0, 0, 0],
  [0, -9, 2, -4, -4, 0],
  [-7, 0, 0, -2, 0, 0],
  [0, 0, -1, -2, -4, 0]
]

def find_sum(arr)
  max_sum = 0
  arr_length = arr.length
  i = 0
  while i < arr_length - 2
    j = 0
    while j < arr_length - 2
      sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i +2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
      (i.zero? && j.zero? || sum > max_sum) && (max_sum = sum)
      j += 1
    end
    i += 1
  end
  max_sum
end

puts findSum(testArr3)
