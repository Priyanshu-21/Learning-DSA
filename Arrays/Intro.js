// Introduction to Arrays in JavaScript

// 1. Find sum of all elements 
let arr = [0, 1, 1, 2, 3, 5, 8, 13]; 

function countElement(arrayElement) {
    let sum = 0; 
    for(let i = 0; i < arrayElement.length; i++) {
        sum += arrayElement[i]; 
    }
    return sum; 
}

//console.log(countElement(arr)); 

// 2. Find Largest Element in Array
let array = [10, -1, 100, 200, 8, 34, 400]; 

function findLargest(array) {
    let largest = 0; 
    for (let i = 0; i < array.length; i++) {
        if(array[i] >= largest) largest = array[i]; 
    }
    return largest; 
}

//console.log(findLargest(array)); 

// 3. Find 3rd largest element 
function findThirdLargest(array) {

    //find largest  
    let largest = 0; 
    for (let i = 0; i < array.length; i++) {
        if(array[i] >= largest) largest = array[i]; 
    }

    //Middle element
    const middle = parseInt(array.length / 2); 
    const middleElement = array[middle]; 

    // left Partition 
    let leftLargest = 0; 
    for (let i = 0; i < middle; i++) {
        if(array[i] >= leftLargest) leftLargest = array[i]; 
    }

    // right Partition 
    let rightLargest = 0; 
    for (let i = middle + 1; i < array.length; i++) {
        if(array[i] >= rightLargest) rightLargest = array[i]; 
    }

    console.log(middleElement, leftLargest, rightLargest);
    return Math.min(largest, middleElement, leftLargest, rightLargest); 
}

//console.log(findThirdLargest(array));

let nums = [0, 1, 2, 0, 3, 0, 4, 5, 0, 9]; 

const n = nums.length; 
let j = n / 2; 
for (let i = 0; i < n / 2; i++) {
    if(j <= n) {
        if(nums[i] === 0 && nums[j] != 0) {
            let temp = nums[j]; 
            nums[j] = nums[i]; 
            nums[i] = temp; 
        }
        j++; 
        console.log(j);
    }
}

console.log(nums); 

