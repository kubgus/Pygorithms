def solution(data, n):
    valid = []
    counters = {}
    for entry in data:
        if entry in counters:
            counters[entry] += 1
        else:
            counters[entry] = 1
    for number, count in counters.items():
        if count <= n:
            valid.append(number)
    print(valid)


solution([1, 1, 1, 1, 3], 1)
