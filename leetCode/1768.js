/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let i = 0
    let j = 0
    let combinedLength = word1.length + word2.length - 1
    let result = []

    while(combinedLength > 0) {
        if(i !== word1.length) {
            result.push(word1[i])
            i++
        }
        if(j !== word2.length) {
            result.push(word2[j])
            j++
        }
        combinedLength--
    }
    return result.join('')
};