from py_sliding_window_maximium import sliding_window_maximium

tests = [
    # (nums, k, expected)
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),   # exemples du sujet
    ([4, 2, 12, 11, -5], 2, [4, 12, 12, 11]),
    ([], 3, []),
    # cas limites supplementaires
    ([1, 2, 3], 0, []),                 # k = 0
    ([1, 2, 3], -1, []),                # k negatif
    ([1, 2], 5, []),                    # k plus grand que la liste
    ([1, 5, 2], 3, [5]),                # k == longueur de la liste
    ([3, 1, 2], 1, [3, 1, 2]),          # k = 1, fenetre de un seul element
    ([2, 2, 2], 2, [2, 2]),             # valeurs identiques
    ([-1, -5, -2], 2, [-1, -2]),        # nombres negatifs
]

if __name__ == "__main__":
    for i, (nums, k, expected) in enumerate(tests, start=1):
        result = sliding_window_maximium(nums, k)
        assert result == expected, f"Test {i} echoue: sliding_window_maximium({nums}, {k}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
