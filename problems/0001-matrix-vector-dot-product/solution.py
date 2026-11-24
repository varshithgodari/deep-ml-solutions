def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if not a or not a[0]:
        return -1

    num_cols = len(a[0])
    if len(b) != num_cols:
        return -1

    return [sum(row_val * vec_val for row_val, vec_val in zip(row, b)) for row in a]