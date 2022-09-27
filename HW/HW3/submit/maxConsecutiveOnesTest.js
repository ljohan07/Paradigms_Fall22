var assert = require('assert');
var max_ones = require('./fixedMaxConsecutiveOnes');

describe('fixedMaxConsecutiveOnes(nums)', function() {
    describe('ends in 1', function() {
        it('should return 2 when nums is [1,0,1,1]', function() {
            assert.equal(max_ones.fixedMaxConsecutiveOnes([1,0,1,1]), 2);
        });
    });
    describe('numbers other than 1', function() {
        it('should return 1 when nums is [0,1]', function() {
            assert.equal(max_ones.fixedMaxConsecutiveOnes([0,1]), 1);
        });
    });
    describe('array of length 1', function() {
        it('should return 1 when nums is [1]', function() {
            assert.equal(max_ones.fixedMaxConsecutiveOnes([1]), 1);
        });
    });
});