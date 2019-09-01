const replaceAt = (string, index, replace) => {
  return string.substring(0, index) + replace + string.substring(index + 1);
}

const toLowerCase = str => {
  const alphaMap = new Map([
      ["A", "a"],
      ["B", "b"],
      ["C", "c"],
      ["D", "d"],
      ["E", "e"],
      ["F", "f"],
      ["G", "g"],
      ["H", "h"],
      ["I", "i"],
      ["J", "j"],
      ["K", "k"],
      ["L", "l"],
      ["M", "m"],
      ["N", "n"],
      ["O", "o"],
      ["P", "p"],
      ["Q", "Q"],
      ["R", "r"],
      ["S", "s"],
      ["T", "t"],
      ["U", "u"],
      ["V", "v"],
      ["W", "w"],
      ["X", "x"],
      ["Y", "y"],
      ["Z", "z"]
  ]);
    let i = str.length - 1
    let arr = str.split('');
    while (i >= 0){
      if (alphaMap.get(str[i])){
        str = replaceAt(str, i, alphaMap.get(str[i]))
      }
      // console.log(str[i])
        i--;
    }
    return str
};

console.log(toLowerCase("Hello"));
