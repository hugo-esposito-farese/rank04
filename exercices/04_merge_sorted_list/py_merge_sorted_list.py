def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    result = []
    for sublist in lists:
        result.extend(sublist)
    result.sort()
    return result
