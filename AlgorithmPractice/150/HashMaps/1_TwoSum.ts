function twoSum(nums: number[], target: number): number[] {
    const prevMap = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];

        if (diff in prevMap) {
            return [prevMap[diff], i];
        }

        prevMap[nums[i]] = i;
    }
};