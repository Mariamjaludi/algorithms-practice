def countCharacters(words, chars):
  good_arr = []
  for word in words:
    str = chars
    good = True
    print("word is",word)
    print ("str is", str)
    for letter in word:
      print("letter is", letter)
      if letter in str:
        index = str.find(letter)
        str = str[:index] + str[(index +1):]
        print("str is", str)
      else:
        good = False
        break

    if good:
      good_arr.append(len(word))

  return sum(good_arr)
