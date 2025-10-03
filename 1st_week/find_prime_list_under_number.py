# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

input = 20

def find_prime_list_under_number(number):
    prime_list = []
    # 이 부분을 채워보세요!
    # 2이상 20이하 자연수 찾기
    for n in range(2, number + 1) :     # number 3
        # 2~20 애들이 소수인지 찾기
        for i in range(2, n) :          # i = 2, n = 3
            if n % i == 0 :
                break;
        else :
            # 소수이면 prime_list에 append
            prime_list.append(n);
    return prime_list


result = find_prime_list_under_number(input)
print(result)