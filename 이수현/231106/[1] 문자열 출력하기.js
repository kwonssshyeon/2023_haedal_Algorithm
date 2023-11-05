const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [rl];

rl.on("line", function (line) {
  input = [line];
  console.log(line);
}).on("close", function () {
  str = input[0];
});
