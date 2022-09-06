function comparison(n){
    if(n > 0){
        var result = "Positive";
    }else if( n == 0){
        var result = "Zero";
    }else{
        let result = "Negative";
    }
    return result;
}
console.log(comparison(1));  // prints "Positive"
console.log(comparison(0));  // prints "Zero"
console.log(comparison(-1)); // prints "undefined"