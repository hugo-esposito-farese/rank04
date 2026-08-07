def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    in_degree = {pkg: 0 for pkg in packages}
    graph = {pkg: [] for pkg in packages}

    for pkg, deps in packages.items():
        for dep in deps:
            if dep not in packages:
                continue
            graph[dep].append(pkg)
            in_degree[pkg] += 1

    available = sorted(pkg for pkg in packages if in_degree[pkg] == 0)
    order = []

    while available:
        current = available.pop(0)
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                available.append(neighbor)
        available.sort()

    if len(order) != len(packages):
        return []
    return order
