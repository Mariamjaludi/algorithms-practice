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

  # i = 0
  # answer = []
  # return answer if nums.length < 2
  #
  # while i < nums.length
  #   diff = target - nums[i]
  #   # binding.pry
  #   j = i + 1
  #   while j < nums.length
  #       if (nums[j] == diff)
  #         # binding.pry
  #           answer[0] = i
  #           answer[1] = j
  #       end
  #       j += 1
  #   end
  #   i += 1
  # end
  # answer
end

puts two_sum(arr, target)
