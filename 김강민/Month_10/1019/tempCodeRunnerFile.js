for (let i = 1; i <= input[0]; i++) {
    let numbers = input[i].split(' ');

    console.log(`Case #${i}: ${Number(numbers[0]) + Number(numbers[1])}`);
}