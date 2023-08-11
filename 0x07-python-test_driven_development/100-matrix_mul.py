#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The result of the matrix multiplication.

    Raises:
        TypeError: If the input matrices are not lists or
        contain invalid elements.
        ValueError: If the input matrices are empty or
        incompatible for multiplication.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row_x in m_a:
        if type(row_x) is not list:
            raise TypeError("m_a must be a list of lists")
    for row_y in m_b:
        if type(row_y) is not list:
            raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for row_x in m_a:
        for m in row_x:
            if not isinstance(m, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row_x) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row_y in m_b:
        for n in row_y:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row_y) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    i = len(m_a)
    j = len(m_a[0])

    a = len(m_b)
    b = len(m_b[0])

    if j != a:
        raise ValueError("m_a and m_b can't be multiplied")

    list_of_lists = []
    for row in range(i):
        row_value = []
        for column in range(b):
            row_value.append(0)
        list_of_lists.append(row_value)

    for x in range(i):
        for q in range(b):
            value = 0
            for p in range(a):
                value += m_a[x][p] * m_b[p][q]
            list_of_lists[x][q] = value

    return list_of_lists
