def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if len(arr1) == 0:
        return True
    doubled = arr1 + arr1
    for i in range(len(arr1)):
        if doubled[i:i + len(arr1)] == arr2:
            return True
    return False
