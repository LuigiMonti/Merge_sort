def merge_two_lists(l1: list, l2: list) -> list:
    result = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i:])
    result.extend(l2[j:])

    return result

# Prueba
l1 = [1, 2, 4]
l2 = [1, 3, 4]
print(merge_two_lists(l1, l2))  # [1, 1, 2, 3, 4, 4]