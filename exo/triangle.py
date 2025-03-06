def triangle(E):
    result = ''
    for i in range(1, E + 1):
        result += '█' * i
    return result.strip()