def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_grater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_grater.append(item)
        else:
            items_lower.append(item)
        
    return quicksort(items_lower) + [pivot] + quicksort(items_grater)