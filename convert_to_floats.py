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

'''
위 코드에서 matrix는 실수로 변환하고자 하는 2차원 리스트를 의미합니다. 
convert_to_floats 함수는 matrix를 인자로 받아, 2중 for 루프를 통해 matrix의 각 원소를 float 함수를 이용하여 실수로 변환한 뒤, 그 값을 다시 matrix에 저장합니다.
마지막으로 변환된 matrix를 반환합니다.
'''
