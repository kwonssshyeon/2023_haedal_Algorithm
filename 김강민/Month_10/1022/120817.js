function solution(numbers) {
    return numbers.reduce((sum, currentNumber) => sum + currentNumber) / numbers.length;
}
