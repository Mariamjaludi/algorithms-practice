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

def findSum(arr)
  maxSum = 0
  arrLength = arr.length
  i = 0
  while (i < arrLength - 2 )
    j = 0
    while (j < arrLength - 2 )
      sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i +2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
      if i === 0 && j === 0 || sum > maxSum
        maxSum = sum
      end
      j += 1
    end
    i += 1
  end
  maxSum
end

puts findSum(testArr3)
