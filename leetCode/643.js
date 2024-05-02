/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += nums[i];
    }
    let left = 0;
    let right = k;

    let max = sum;

    // sliding window algoritmas
    while (right < nums.length) {
        
        sum -= nums[left]; // panaikina elementa nuo kaires
        left++;

        sum += nums[right];
        right++;

        max = Math.max(max, sum); // suranda didziausia suma
    }
    return parseFloat((max / k).toFixed(4));
};