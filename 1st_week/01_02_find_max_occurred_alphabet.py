def find_alphabet_occurrence_array(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26  # [0, 0, 0, 0, 0, . . ., 0]

    # 받은 문자열의 길이만큼 반복
    for i in range(0, len(string)) :
        if string[i].isalpha() == True :
            # 첫번째문자부터 아스키코드로 치환하고 인덱싱을위해 기본값 97을 뺌
            alphabet_occurrence_index = ord(string[i]) - ord('a')
            # print(alphabet_occurrence_index)
            # 나온값을 초기화했던 배열에 업데이트
            alphabet_occurrence_array[alphabet_occurrence_index] += 1
        else :
            continue

    return alphabet_occurrence_array


# print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 =",
#       find_alphabet_occurrence_array("hello my name is dingcodingco"))
# print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 =",
#       find_alphabet_occurrence_array("we love algorithm"))
# print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 =",
#       find_alphabet_occurrence_array("best of best youtube"))


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    # find_alphabet_occurrence_array에 문자열을 넣고 출력받은 배열
    find_alphabet_occurrence_array(string)  # [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]

    # 그 배열에서 가장 큰 값을 찾음
    arr = find_alphabet_occurrence_array(string)
    max_index = 0;
    max_occurred_alphabet_num = find_alphabet_occurrence_array(string)[0];

    for i in range(0, len(arr)) :
        if max_occurred_alphabet_num < arr[i] :
            max_occurred_alphabet_num = arr[i]
            max_index = i

    # 26개의 배열중 가장 큰 값을 찾았으면
    return chr(max_index + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))