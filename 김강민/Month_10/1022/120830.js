function solution(n, k) {
    let answer = 0;
    const sheep = 12000;
    const drink = 2000;

    if (n >= 10) {
        answer = sheep * n + drink * (k - Math.floor(n / 10));
    } else {
        answer = sheep * n + drink * k;
    }
    return answer;
}
