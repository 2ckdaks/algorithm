# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

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

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    array = find_alphabet_occurrence_array(string)  # [0, 3, 2, 4... , 2]
    index = []  # [0, 2]
    alphbet = []  #[a, b]
    print_alphabet = "_"

    # 반복되지않는 알파벳의 index
    for i in range(0, len(array)) :
        if array[i] == 1 :
            index.append(i);

    for i in range(0, len(index)) :
        alphbet.append(chr(index[i] + ord('a')));

    # 어떤 반복되지않는 알파벳이 먼저 나왔는지
    for i in range(0, len(string)) :
        for j in range(0, len(alphbet)) :
            if string[i] == alphbet[j] :
                print_alphabet = string[i]

        if print_alphabet != "_" :
            break;

    return print_alphabet


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))