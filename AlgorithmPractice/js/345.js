/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = {}; // {a: True, ... , A = true, ...}
    for (const char of "aeiouAEIOU" ) {
        vowels[char] = true;
    }

    const characters = s.split("");

    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        while (left < right && !(s[left]) in vowels) {
            left += 1;
        }   
        while (left < right && !(s[right]) in vowels) {
            right -= 1;
        }
        
        swap(characters, left, right);
        left += 1;
        right -= 1;
    }
    return characters.join("");
};

function swap(arr, i, j) {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}