function f1(){
    let x = 10;
    function f2(fx){
        let x;
        x = 6;
        fx();
    };

    function f3(){
        console.log(x);
    };

    f2(f3);
};

f1();