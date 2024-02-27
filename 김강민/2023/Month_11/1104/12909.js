function solution(s){
    let count = 0;
    for(let i = 0; i < s.length; i++) {
        if (s[i] === '(') count += 1;
        if (s[i] !== '(') count += -1;
        
        if (count < 0) return false;
    }
    if (count === 0) answer = true
    if (count !== 0) answer = false
    return answer;
}