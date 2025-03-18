function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const countS = new Map<string, number>();
    const countT = new Map<string, number>();

    for (let i = 0; i < s.length; i++) {
        const charS = s[i];
        const charT = t[i];

        countS.set(charS, (countS.get(charS) || 0) + 1);
        countT.set(charT, (countT.get(charT) || 0) + 1);
    }

    for (let [key, value] of countS) {
        if (countT.get(key) !== value) {
            return false;
        }
    }

    return true;
};