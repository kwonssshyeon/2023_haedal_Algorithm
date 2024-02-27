function solution(numbers) {
    const answer = [];

    for (let i = 0; i < numbers.length; i++) {
        const temp = numbers[i] * 2;
        answer.push(temp);
    }

    return answer;
}
