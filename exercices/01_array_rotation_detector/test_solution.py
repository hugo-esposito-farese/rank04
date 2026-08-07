from py_array_rotation_detector import array_rotation_detector

tests = [
    # (arr1, arr2, expected)
    ([1, 2, 3, 4, 5], [4, 5, 1, 2, 3], True),   # exemples du sujet
    ([1, 2, 3, 4, 5], [5, 1, 2, 3, 4], True),
    ([1, 2, 3], [3, 2, 1], False),
    ([1, 2], [1, 2, 3], False),
    ([], [], True),
    # cas limites supplementaires
    ([1], [1], True),                            # un seul element
    ([1], [2], False),                           # un seul element different
    ([1, 2, 3], [1, 2, 3], True),                # rotation de 0 (identique)
    ([1, 1, 1], [1, 1, 1], True),                # doublons, toujours vrai
    ([1, 2, 1, 2], [2, 1, 2, 1], True),          # doublons, vraie rotation
    ([1, 2, 1, 3], [1, 3, 1, 2], True),          # doublons, rotation valide
    ([1, 2, 3, 4], [2, 1, 3, 4], False),         # permutation mais pas rotation
    ([-1, -2, -3], [-3, -1, -2], True),          # nombres negatifs
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], False),   # meme longueur, pas une rotation
]

if __name__ == "__main__":
    for i, (arr1, arr2, expected) in enumerate(tests, start=1):
        result = array_rotation_detector(arr1, arr2)
        assert result == expected, f"Test {i} echoue: array_rotation_detector({arr1}, {arr2}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
