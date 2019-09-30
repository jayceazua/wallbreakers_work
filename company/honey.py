def solution(N, K):
    if N <= 0:
        return [""]
    result = []
    for p in solution(N - 1, K):
        print(p)
        for l in "abc":
            if p[-1:] != l:
                result.append(p + l)
    return result[:K]


print(solution(2, 2))