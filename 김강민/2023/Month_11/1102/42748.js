function solution(array, commands) {
    let result = [];
    let i = 0;
    let j = 0;
    let k = 0;

    for (let n = 0; n < commands.length; n++) {
        i = commands[n][0];
        j = commands[n][1];
        k = commands[n][2];

        let sliced = array.slice(i - 1, j);
        let sorted = sliced.sort((a, b) => a - b);

        result.push(sorted[k - 1]);
    }

    return result;
}
