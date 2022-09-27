var assert = require('assert');
var parityAnalysisTest = require('./parityAnalysis')

describe('parityAnalysis(n)', function() {
    describe('all odds', function() {
        it('should return false since 35 is odd but digit sum is even', function() {
            assert.equal(parityAnalysisTest.parityAnalysis(35), false);
        });
    });
    describe('odd number in the middle', function() {
        it('should be false, number is even but digit sum is odd', function() {
            assert.equal(parityAnalysisTest.parityAnalysis(2661662), false);
        });
    });
    describe('testing number with 0s', function() {
        it('testing presence of 0s, should be false', function() {
            assert.equal(parityAnalysisTest.parityAnalysis(920041), false);
        });
    });
    describe('even number in the middle - even number of odd numbers', function() {
        it('should be false', function() {
            assert.equal(parityAnalysisTest.parityAnalysis(5552555), false);
        });
    });
    describe('even number in the middle - odd number of odd numbers', function() {
        it('should be true', function() {
            assert.equal(parityAnalysisTest.parityAnalysis(552555), true);
        });
    });
});