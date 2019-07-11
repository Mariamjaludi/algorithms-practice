# Complete the sockMerchant function below.
def findPairs(ar, find, pairs)
# check if array is empty. If it is, function will
# return pairs value as is.
  unless ar.empty?
    newAr = ar
    # check if there is a pair in the array
    # if there is a pair, increment pairs and
    # remove pair from array
    if newAr.index(find)
      pairs += 1
      # remove found pair
      newAr = [*newAr.slice(0, newAr.index(find)), *newAr[(newAr.index(find) + 1)..-1]]
    end
    # recursive call to find pairs until no pairs are found
    return findPairs(newAr.drop(1), newAr[0], pairs)
  end
  pairs
end

def sockMerchant(_n, ar)
  pairs = 0
  find = ar[0]
  findPairs(ar.drop(1), find, pairs)
end
