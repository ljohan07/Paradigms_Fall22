for (var i = 0; i < 3; i++) {
    setTimeout( () => console.log(i), 100 )
}
for (let i = 0; i < 3; i++) {
    setTimeout( () => console.log(i), 100 )
}

for (var i = 0; i < 3; i++) {
    setTimeout( () => console.log(x), 100 )
}
x = 10;