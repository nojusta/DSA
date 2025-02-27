// mano sprendimas:

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let k = 0;
    let s_char = s.split("");
    let t_char = t.split("");

    for (let i = 0; i < s.length; i++) {
        let found = false;
        for(let j = k; j < t.length; j++) {
            if(t_char[j] === s_char[i]) {
                k = j + 1;
                found = true;
                break;
            }
        }
        if(!found) return false;
    }
    return true;
};

// geresnis sprendimas:

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let i = 0;
    let j = 0;

    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            i++;
        }
        j++;
    }

    return i === s.length;
};