// Booyer-Moore Majority Voting Method 
let nums = [2, 2, 1, 2, 1, 1, 2, 0]; 
let count = 0; 
let candidate = null; 

for (let i = 0; i < nums.length; i++) {
    if(count === 0) {
        candidate = nums[i]; 
    }

    count += (nums[i] === candidate)? +1: -1; 
}

console.log(candidate, count);