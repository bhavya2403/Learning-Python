def acmTeam(topic):
    max_topics = []
    topL = len(topic)
    for i in range(topL-1):
        for j in range(i+1, topL):
            summ = list(str(int(topic[i]) + int(topic[j])))
            max_topics.append(summ.count('2') + summ.count('1'))

    return [max(max_topics), max_topics.count(max(max_topics))]


print(acmTeam(['10101', '11100', '11010', '00101']))
