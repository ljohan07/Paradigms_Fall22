target = 4;
i = 0;
let j = 0;

for (; i <= 4; i++) {
    console.log(`i ${i}`)
    for (j = 0; j <= 4; j++) {
        console.log(`j ${j}`)
        if (i*j === target) {
            console.log('here')
            break;
        }
    }
}

console.log(`Values at break out are ${i}, ${j}`)