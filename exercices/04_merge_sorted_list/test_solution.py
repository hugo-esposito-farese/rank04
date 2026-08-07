from py_merge_sorted_list import merge_sorted_list

tests = [
    # (lists, expected)
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),  # exemples du sujet
    ([[1, 2, 3], [], [0, 4]], [0, 1, 2, 3, 4]),
    ([], []),
    ([[], []], []),
    # cas limites supplementaires
    ([[5]], [5]),                                                 # une seule sous-liste
    ([[-3, -1], [-2, 0]], [-3, -2, -1, 0]),                       # nombres negatifs
    ([[2, 2, 2], [2, 2]], [2, 2, 2, 2, 2]),                       # doublons conserves
    ([[9, 8, 7]], [7, 8, 9]),                                     # sous-liste censee etre triee mais on trie quand meme
]

if __name__ == "__main__":
    for i, (lists, expected) in enumerate(tests, start=1):
        result = merge_sorted_list(lists)
        assert result == expected, f"Test {i} echoue: merge_sorted_list({lists}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
