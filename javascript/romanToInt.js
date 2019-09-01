
const romanToInt = s => {
  if (s.length === 0){
    return 0;
  }

  const map = new Map([
    ['I', 1],
    ['V', 5],
    ['X', 10],
    ['L', 50],
    ['C', 100],
    ['D', 500],
    ['M', 1000]
  ]);

  // const map = {
  //   I: 1,
  //   V: 5,
  //   X: 10,
  //   L: 50,
  //   C: 100,
  //   D: 500,
  //   M: 1000
  // };

  let i = s.length - 1;
  let result = map.get(s[i]);

  while (i > 0) {
    const current = map.get(s[i]);
    const previous = map.get(s[i - 1]);

    if (previous >= current) {
      result += previous;
    } else {
      result -= previous;
    }
    i--;
  }
  return result;
};


s = "III"

console.log(romanToInt(s))
