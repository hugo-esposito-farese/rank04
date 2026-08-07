def palindrome_partitioner(s: str) -> int:
    if not s or s == s[::-1]:
        return 0

    mini = len(s)

    for i in range(1, len(s)):
        gauche = s[:i]
        droite = s[i:]
        if gauche == gauche [::-1]:
            mini = min(mini, 1 + palindrome_partitioner(droite))
    return mini