const removeElement = (nums, val) => {
    let i = 0
    let j = 0
    while (j < nums.length) {
      if(nums[j] != val){
        nums[i] = nums[j];
        i++;
      }
      j++;
    }
  return i
};

nums = [3,2,2,3];
val = 3;

console.log(removeElement(nums, val))
