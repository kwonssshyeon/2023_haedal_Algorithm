let read = require('fs').readFileSync('/dev/stdin');
let input = read.toString().trim().split('\n');

for (let i = 1; i <= input[0]; i++) {
    let numbers = input[i].split(' ').map(Number);
    console.log(`Case #${i}: ${numbers[0] + numbers[1]}`);
}
