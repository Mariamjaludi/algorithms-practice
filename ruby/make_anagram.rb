# def makeAnagram(a, b)
#     deleted = 0
#     if a > b
#         test_word = b.chars
#         iterator = a
#     else
#         test_word = a.chars
#         iterator = b
#     end
#     iterator.chars.each do |c|
#         if test_word.include?(c)
#             test_word = test_word.filter{ |char| char != c }
#             # this will leave the letters that dont match in the shorter string
#         else
#             deleted += 1
#         end
#     end
#     deleted = deleted + test_word.length
# end
require 'pry'
def makeAnagram(a, b)
    alpha = 'abcdefghijklmnopqrstuvwxyz'.split('')
    letter_count_a = alpha.map {|l| a.count(l)}
    letter_count_b = alpha.map {|l| b.count(l)}
    i = 0
    deleted = 0
    while i < letter_count_a.length
      deleted = deleted + (letter_count_a[i] - letter_count_b[i]).abs
      i += 1
    end
    deleted
end

# test cases
a = "bugexikjevtubidpulaelsbcqlupwetzyzdvjphn"
b = "lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk"

c = 'fsqoiaidfaukvngpsugszsnseskicpejjvytviya'
d = 'ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget'
puts makeAnagram(a, b)
puts makeAnagram(c, d)
