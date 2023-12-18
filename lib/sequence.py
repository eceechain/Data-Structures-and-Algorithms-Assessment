
# remove_duplicates.py

def remove_duplicates(sequence):
    """
    Removes duplicates from the given sequence (list or tuple) while preserving the original order.
    Returns a new sequence without duplicates.
    """
    seen = set()  # Set to keep track of seen elements
    result = []  # Resultant list without duplicates

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Testing
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
