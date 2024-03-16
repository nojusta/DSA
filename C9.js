function lookAndSay(A, n) {
    let result = [A.toString()]; 

    while (result.length < n) {
        let previous = result[result.length - 1]; // paskutinis elementas
        let next = ''; 
        let count = 1;

        for (let j = 1; j <= previous.length; j++) { // eina per kiekviena elementa/skaiciu "previous" stringe 
            if (previous[j] === previous[j - 1]) {
                count++;
            } else {
                next += count.toString() + previous[j - 1];
                count = 1;
            }
        }

        result.push(next);
    }

    return result;
}

let A = 1; // pradinis narys 
console.log(lookAndSay(A, 10));