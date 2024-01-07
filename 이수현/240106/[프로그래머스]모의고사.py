def solution(answers):
    answer = [0, 0, 0]
    one_answer, two_answer = 0, 0
    three_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    two_answerary = [1, 3, 4, 5]
    idx = 0
    new_answer = []

    for i in range(0, len(answers)):
        one_answer = (one_answer % 5) + 1
        if i % 2 == 0:
            two_answer = 2
        else:
            two_answer = two_answerary[idx]
            idx = (idx + 1) % 4
        if one_answer == answers[i]:
            answer[0] += 1
        if two_answer == answers[i]:
            answer[1] += 1
        if three_answer[i % 10] == answers[i]:
            answer[2] += 1

    max_num = max(max(answer[0], answer[1]), answer[2])
    for i in range(len(answer)):
        if answer[i] == max_num:
            new_answer.append(i + 1)

    return new_answer
