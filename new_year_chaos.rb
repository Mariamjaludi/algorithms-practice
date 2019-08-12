#!/bin/ruby

require 'json'
require 'stringio'

# Complete the minimumBribes function below.
def minimumBribes(q)
  i = q.length - 1
  bribes = 0
  while i >= 0
    #if a value is in a position greater than value - or + 3 it is chaotic
    if q[i] - i > 3
      return "Too chaotic"
    end

    j = 0 > q[i] - 2 ? 0 : (q[i] - 2)
    while j < i
      if (q[j] > q[i])
        bribes += 1
      end
      j += 1
    end
    i -= 1
  end
  bribes
end

t = gets.to_i

t.times do |t_itr|
    n = gets.to_i

    q = gets.rstrip.split(' ').map(&:to_i)

    puts minimumBribes q
end
