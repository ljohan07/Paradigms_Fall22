function findMaxConsecutiveOnes(nums) {
    var max_count = 0;
    var start = 0;
    var end = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != 1) {
            let curr_count = end - start;
            if (curr_count > max_count) {
                max_count = curr_count;
            }
            start = i + 1
        }
        end = i + 1;
    }
    if (end - start > max_count) {
        max_count = end - start;
    }
    return max_count;
}

// console.log(findMaxConsecutiveOnes([1,1,10,1,1,1]))
// console.log(findMaxConsecutiveOnes([1,0,1,1,0,1]))
// console.log(findMaxConsecutiveOnes([1,-10,1,1,8,1,1,1,9,1,1,1,1,1,1]))
// console.log(findMaxConsecutiveOnes([1,1,5,1,1,1]))
module.exports = {findMaxConsecutiveOnes}