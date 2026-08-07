from py_constellation_mapper import constellation_mapper

tests = [
    # (stars, size, expected)
    ([(0, 0), (1, 1), (2, 2)], 3, ["*..", ".*.", "..*"]),   # exemples du sujet
    ([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3, ["***", ".*.", "..*"]),
    ([(0, 0), (5, 5), (2, 2)], 3, ["*..", "...", "..*"]),
    ([(0, 0), (5, 5)], 2, ["*.", ".."]),
    # cas limites supplementaires
    ([], 3, ["...", "...", "..."]),                          # aucune etoile
    ([(0, 0), (0, 0), (0, 0)], 2, ["*.", ".."]),              # doublons exacts
    ([(-1, 0), (0, -1), (10, 10)], 3, ["...", "...", "..."]), # coordonnees negatives/hors grille
    ([(0, 0)], 1, ["*"]),                                     # grille 1x1
    ([(2, 0), (0, 2)], 3, ["..*", "...", "*.."]),             # coins
    ([], 0, []),                                              # grille vide
]

if __name__ == "__main__":
    for i, (stars, size, expected) in enumerate(tests, start=1):
        result = constellation_mapper(stars, size)
        assert result == expected, f"Test {i} echoue: constellation_mapper({stars}, {size}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
