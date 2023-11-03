function solution(numbers) {
    const number = { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9 };
    let temp = '';
    let answer = '';

    [...numbers].forEach((element) => {
        temp += element;
        if (number[temp] >= 0) {
            answer += number[temp];
            temp = '';
        }
    });
    return parseInt(answer);
}
