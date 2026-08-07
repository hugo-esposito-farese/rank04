from py_palindrome_partitioner import palindrome_partitioner

tests = [
    # (s, expected)
    ("aab", 1),        # exemples du sujet
    ("aba", 0),
    ("abc", 2),
    # cas limites supplementaires
    ("", 0),                 # chaine vide
    ("a", 0),                # un seul caractere
    ("aa", 0),               # deja un palindrome
    ("ab", 1),                # deux caracteres differents
    ("racecar", 0),           # palindrome complet
    ("abccba", 0),            # palindrome complet pair
    ("aaaa", 0),              # tous identiques
    ("abcde", 4),             # tous distincts -> len(s) - 1
    ("aabb", 1),              # "aa" + "bb"
]

if __name__ == "__main__":
    for i, (s, expected) in enumerate(tests, start=1):
        result = palindrome_partitioner(s)
        assert result == expected, f"Test {i} echoue: palindrome_partitioner({s!r}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
