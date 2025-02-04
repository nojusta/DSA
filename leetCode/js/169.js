/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let counts = {};
    let majorityCount = nums.length / 2;

    for(let num of nums) {
        if (!counts[num]) {
            counts[num] = 1;
        } else {
            counts[num]++;
        }

        if (counts[num] > majorityCount) {
            return num;
        }
    }
};
console.log("Deivi padaryk man sumustini pls :3");