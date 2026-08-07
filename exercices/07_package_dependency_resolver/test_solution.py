from package_dependency_resolver import package_dependency_resolver

tests = [
    # (packages, expected)
    ({"app": ["database"], "database": ["driver"], "driver": []}, ["driver", "database", "app"]),  # exemples du sujet
    ({"A": [], "B": ["A"], "C": ["A", "B"]}, ["A", "B", "C"]),
    ({}, []),
    ({"X": ["Y"], "Y": ["X"]}, []),
    ({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}, ["api", "backend", "web", "frontend"]),
    # cas limites supplementaires
    ({"A": ["A"]}, []),                                                  # auto-dependance
    ({"A": [], "B": []}, ["A", "B"]),                                    # paquets independants, ordre alphabetique
    ({"A": ["Z"]}, ["A"]),                                               # dependance vers un paquet inexistant, ignoree
    ({"A": [], "B": ["A"], "C": ["A"], "D": ["B", "C"]}, ["A", "B", "C", "D"]),  # dependances en losange
    ({"A": ["B"], "B": ["C"], "C": ["A"]}, []),                          # cycle de longueur 3
]

if __name__ == "__main__":
    for i, (packages, expected) in enumerate(tests, start=1):
        result = package_dependency_resolver(packages)
        assert result == expected, f"Test {i} echoue: package_dependency_resolver({packages}) = {result}, attendu {expected}"
    print(f"Tous les tests ({len(tests)}) sont passes avec succes.")
