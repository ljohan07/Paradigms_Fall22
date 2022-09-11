var assert = require('assert');
var demoQ2 = require('./question2')

describe('findMaxConsecutiveOnes(nums)', function() {
    describe('all positive args', function() {
        it('should return 4 when nums is [1,1,1,1,0,0,1,0,1,1,0,10,111111111]', function() {
            assert.equal(demoQ2.findMaxConsecutiveOnes([1,1,1,1,0,0,1,0,1,1,0,10,111111111]), 4);
        });
    });
    describe('some negative args', function() {
        it('should return 1 when nums is [1,-1,1,-1,1,-1,1,10]', function() {
            assert.equal(demoQ2.findMaxConsecutiveOnes([1,-1,1,-1,1,-1,1,10]), 1);
        });
    });
});