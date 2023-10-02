const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
// const input = fs.readFileSync("input.txt").toString().trim();

let sum = 0;
let n = 0;

while (true) {
  n++;
  sum += n;
  if (sum >= input) break;
}

if (n % 2 === 0) {
  // 짝수번째 합일 때
  const numerator = input - (sum - n); // 분자
  const denominator = n + 1 - numerator; // 분모
  console.log(`${numerator}/${denominator}`);
} else {
  // 홀수번째 합일 때
  const denominator = input - (sum - n); // 분모
  const numerator = n + 1 - denominator; // 분자
  console.log(`${numerator}/${denominator}`);
}
