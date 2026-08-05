def find(scores, target):
    low = 0
    high = len(scores) - 1
    result = -1  

    while low <= high:
        mid = (low + high) // 2

        if scores[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


scores = [0.12, 0.35, 0.41, 0.58, 0.63, 0.77, 0.89, 0.95]

targets = [0.5, 0.9, 0.1, 1.0, 0.41]

for target in targets:
    index = find(scores, target)
    print(f"Target: {target:<4} -> Index: {index}")