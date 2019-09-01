require 'pry'
 x = -123

 def reverse(x)
   y = x.abs.to_s.reverse.to_i
    if y > (2 ** 31 - 1)
        return 0
    elsif x.positive?
        return y
    elsif -y > -(2 ** 31)
        return (0 - y)
    end
 end

 puts reverse(x)
