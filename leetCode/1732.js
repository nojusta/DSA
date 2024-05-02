/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let maxValue = 0;
    let sum = 0;
    for(let i = 0; i < gain.length; i++) {
        sum += gain[i];
        maxValue = Math.max(maxValue, sum);
    }
    return maxValue;
};