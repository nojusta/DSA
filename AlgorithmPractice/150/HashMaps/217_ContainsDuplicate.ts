function containsDuplicate(nums: number[]): boolean {
    if (nums.length == 0) {
        return false;
    }

    const hashMap = new Map<number, number>(); // number : count

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in hashMap) {
            return true;
        }

        hashMap[nums[i]]++;
    }

    return false;
};