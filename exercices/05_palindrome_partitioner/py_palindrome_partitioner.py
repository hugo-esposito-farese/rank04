def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0

    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True

    min_cuts = [0] * n
    for i in range(n):
        if is_palindrome[0][i]:
            min_cuts[i] = 0
        else:
            best = i
            for j in range(i):
                if is_palindrome[j + 1][i] and min_cuts[j] + 1 < best:
                    best = min_cuts[j] + 1
            min_cuts[i] = best

    return min_cuts[n - 1]
