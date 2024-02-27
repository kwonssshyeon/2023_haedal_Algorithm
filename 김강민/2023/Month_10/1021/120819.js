function solution(money) {
    const answer = [];
    const americano = 5500;

    answer[0] = Math.floor(money / americano);
    answer[1] = money % americano;

    return answer;
}
