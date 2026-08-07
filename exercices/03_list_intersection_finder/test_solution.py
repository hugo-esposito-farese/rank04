from py_list_intersection_finder import list_intersection_finder

tests = [
    # (lists, expected)
    ([[1, 2, 3], [2, 3, 4], [2, 3, 5]], [2, 3]),          # exemples du sujet
    ([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]], [4]),
    ([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]], [1, 2, 3]),
    ([[1, 2, 3], [4, 5, 6]], []),
    ([], []),
    ([[1, 2, 3], []], []),
    ([[5]], [5]),
    # cas limites supplementaires
    ([[3, 1, 2], [2, 3]], [2, 3]),                         # listes non triees en entree
    ([[1, 2], [1, 2], [1, 2]], [1, 2]),                    # listes identiques
    ([[-3, -1, 0], [-1, 0, 5]], [-1, 0]),                  # nombres negatifs
    ([[1, 2, 3]], [1, 2, 3]),                              # une seule liste
]

if __name__ == "__main__":
    for i, (lists, expected) in enumerate(tests, start=1):
        result = list_intersection_finder(lists)
        assert result == expected, f"Test {i} echoue: list_intersection_finder({lists}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
