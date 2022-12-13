class GameState{
    constructor(good_letters, bad_letters, correct_letters){
        this.good_letters = good_letters;
        this.bad_letters = bad_letters;
        this.correct_letters = correct_letters;
    } 
}
    
    
function wordleMatches(state, words, is_common) {
    let curr_matches;
    // get good letter matches
    for (let i = 0; i < state.good_letters.length; i++) {
        if (i > 0) {
            curr_matches = curr_matches.filter( (word) => word.includes(state.good_letters[i]) )
        }
        else {
            curr_matches = words.filter( (word) => word.includes(state.good_letters[i]) )
        }
    }
    // get rid of bad letter words
    for (let i = 0; i < state.bad_letters.length; i++) {
        curr_matches = curr_matches.filter( (word) => !word.includes(state.bad_letters[i]) )
    }
    // get correct positioning
    for (let i = 0; i < state.correct_letters.length; i++) {
        if (state.correct_letters[i] != undefined) {
            if (is_common) {
                curr_matches = curr_matches.filter( (word) => word[i+1] == state.correct_letters[i] )
            }
            else {
                curr_matches = curr_matches.filter( (word) => word[i] == state.correct_letters[i] )
            }
        }
    }
    if (is_common) {
        curr_matches = curr_matches.map( (word) => word.substring(1) )
    }
    return curr_matches.sort()
}

function wordleHelper(state){
    fs = require('fs');
    let words = fs.readFileSync('five-letter-words.txt', 'utf8');
    words = words.split('\n')
    console.log(words.length)
    console.log(typeof(words))
    let common_words = words.filter( (word) => word.includes('*') )
    let other_words = words.filter( (word) => !word.includes('*') )
    
    console.log(state)
    common_matches = wordleMatches(state, common_words, true)
    uncommon_matches = wordleMatches(state, other_words, false)
    all_matches = common_matches.concat(uncommon_matches)
    
    return all_matches
 }
/*
state1 = {
    good_letters:["S", "A", "R", "G"],
    bad_letters: ["H", "D", "J", "N", "L", "M", "O", "Z"], 
    correct_letters:["S", undefined, "G", undefined, undefined]
}

state2 = {
    good_letters:["O","A", "J"],
    bad_letters: ["Q","W","E","R","T","Y","M", "K", "N"], correct_letters:[undefined, undefined, undefined, undefined, undefined]
}

console.log(wordleHelper(state1))
console.log(wordleHelper(state2))*/
