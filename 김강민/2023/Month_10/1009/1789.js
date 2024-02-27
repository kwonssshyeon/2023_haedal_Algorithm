let input = require('fs')
    .readFileSync('/dev/stdin')
    .toString()
    .trim()
    .split('\n')
    .map((e) => e.split(' ').map(Number));

let s = input[0];

let total = 0;
let arr = [];
let cnt = 0;

while (total <= s) {
    if (cnt === 0) {
        cnt += 1;
        total += 1;
    } else {
        arr.push(cnt);
        cnt += 1;
        total += cnt;
    }
}

console.log(arr.length);
