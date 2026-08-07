def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common = common & set(lst)
    return sorted(common)
