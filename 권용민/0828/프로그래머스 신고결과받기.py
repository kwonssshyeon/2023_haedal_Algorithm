def solution(id_list, reports, k):
    who_reported_me: dict[str, list[str]] = {}
    for id in id_list:
        who_reported_me[id] = []

    report_counts: dict[str, int] = {}
    for id in id_list:
        report_counts[id] = 0

    mail_counts: dict[str, int] = {}
    for id in id_list:
        mail_counts[id] = 0

    for report in reports:
        reporter, reportee = report.split()
        if reporter not in who_reported_me[reportee]:
            who_reported_me[reportee].append(reporter)
            report_counts[reportee] += 1

    for id in id_list:
        if report_counts[id] >= k:
            for reporter in who_reported_me[id]:
                mail_counts[reporter] += 1

    return list(mail_counts.values())

'''
같은 원소가 없을 때 추가 => set으로 대체 가능
굳이 자료형 따로 만들지 않고 reports 내부 그대로 활용하면 코드가 더 간결해짐

모범답안:

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
'''