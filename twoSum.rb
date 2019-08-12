require 'pry'

arr = [2, 7, 11, 15]
target = 9


def two_sum(nums, target)
  return [] if nums.length < 2
  hash = {}
  for i in (0..nums.length - 1)
    return [hash[target - nums[i]], i] if (hash[target - nums[i]] && hash[target - nums[i]] != i)
    hash[nums[i]] = i
  end
  []
end

puts two_sum(arr, target)
