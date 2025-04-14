let map = new Map(); 
let nums = [2, 3, 1, 2, 3, 2, 2];  

for (let i = 0; i < nums.length; i++) {
    if(!map.has(nums[i])) { 
        map.set(nums[i], 0);
    }   
    let value = map.get(nums[i]);
    map.set(nums[i], value + 1);
}

let element = 0; 
let highestElement = 0; 
for (let [key, value] of map) {
    if (value > highestElement) {
        highestElement = value; 
        element = key; 
    }
}


console.log(map, element, highestElement);