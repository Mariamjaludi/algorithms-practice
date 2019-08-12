/* Returns either the index of the location in the array,
  or -1 if the array did not contain the targetValue */

const binarySearch = (arr, target) => {
  let min = 0;
  let max = arr.length - 1 ;
  let guess;

  while (max >= min){
    guess = Math.floor((min + max) / 2)
    if (array[guess] === targetValue){ return guess;}
    else if (array[guess] < targetValue){ min = guess + 1; }
    else { max = guess - 1;}
  }
  return -1;
}
