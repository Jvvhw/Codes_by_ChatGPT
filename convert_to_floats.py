def convert_to_floats(matrix):
    """
    2차원 리스트의 모든 원소를 실수로 변환하는 함수
    :param matrix: 실수로 변환하고자 하는 2차원 리스트
    :return: 모든 원소가 실수로 변환된 2차원 리스트
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
    return matrix
