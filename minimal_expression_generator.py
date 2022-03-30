# minterm expression을 입력으로 받아, sum of products 형태의 minimal expression을 계산하는 프로그램
# Quine mccluskey method 사용

import pandas as pd

# 두 binary 문자열을 비교하여, 하나만 다를 때 둘을 결합한 걸 반환하고, 하나 이상 다르거나 같다면 -1을 반환하도록 한 함수
def binary_compare(bin1, bin2, num_of_variable):
    compare_count = 0;
    bin_list_1 = list(bin1)
    bin_list_2 = list(bin2)
    bin_list_return = []
    for i in range(0, num_of_variable):
        if bin_list_1[i] != bin_list_2[i]:
            compare_count += 1
            bin_list_return.append('-')
        else:
            bin_list_return.append(bin_list_1[i])

    if compare_count == 1:
        return ''.join(bin_list_return)
    else:
        return -1

# column의 모든 원소들을 비교해 결합 가능한 것들로 다음 column을 만드는 함수
def make_new_column(input_column, new_column, num_of_variable):
    input_col_len = len(input_column)
    for i in range(0, input_col_len - 1):
        for j in range(i + 1, input_col_len):
            compare_return = binary_compare(input_column[i][1], input_column[j][1], num_of_variable)
            if compare_return != -1:
                new_column.append([input_column[i][0] + input_column[j][0], compare_return])
                if len(input_column[i]) == 2:
                    input_column[i].append("V")
                if len(input_column[j]) == 2:
                    input_column[j].append("V")

# binary를 abcd와 '을 사용한 형태로 변환해주는 함수
def binary_to_abc(bin):
    temp = list(bin)
    num_of_variable = len(bin)
    result = []
    char_a = 97
    for i in range(0, num_of_variable):
        if temp[i] == '1':
            result.append(chr(char_a))
        elif temp[i] == '0':
            result.append(chr(char_a) + '\'')
        char_a += 1
    result = "".join(result)
    return result

# -------------------- main --------------------

# minterm expression 입력받음
while 1:
    try:
        minterm_expression_input = str(input("minterm expression을 입력하세요: "))
        minterm_expression_input = minterm_expression_input.replace(' ', '')
        minterm_expression_decimal_str = minterm_expression_input.split(',')
        minterm_expression_decimal_int = list(map(int, minterm_expression_decimal_str))
    except:
        print("다시 입력하세요")
    else:
        break

# 변수 개수 입력받음
while 1:
    try:
        num_of_variable = int(input("변수의 개수를 입력하세요: "))
    except:
        print("정수로 다시 입력하세요")
    else:
        break

minterm_expression_binary_str = []

# minterm을 binary로 변환
for i in minterm_expression_decimal_int:
    minterm_expression_binary_str.append(format(i, 'b').zfill(num_of_variable))

# 비교하여 저장할 column들 생성
column_1 = []
column_2 = []
column_3 = []
column_4 = []
column_5 = []
column_6 = []
column_7 = []
column_8 = []
column_9 = []

# 첫번째 column 생성
for i in range(0, len(minterm_expression_binary_str)):
    column_1.append([[minterm_expression_decimal_int[i]], minterm_expression_binary_str[i]])

print(f"\ninput으로 binary 생성 : \n {column_1}")
# 더이상 결합이 안될 때 까지 생성
make_new_column(column_1, column_2, num_of_variable)
if column_2 != []:
    make_new_column(column_2, column_3, num_of_variable)
    if column_3 != []:
        make_new_column(column_3, column_4, num_of_variable)
        if column_4 != []:
            make_new_column(column_4, column_5, num_of_variable)
            if column_5 != []:
                make_new_column(column_5, column_6, num_of_variable)
                if column_6 != []:
                    make_new_column(column_6, column_7, num_of_variable)
                    if column_7 != []:
                        make_new_column(column_7, column_8, num_of_variable)
                        if column_8 != []:
                            make_new_column(column_8, column_9, num_of_variable)

# 더 결합할 수 없는 항들을 저장할 prime_implicants
prime_implicants = []

columns = [column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8, column_9]
col_num = 1

# 다음 것으로 결합하면 v를 추가하여 리스트의 길이가 3일것이므로, 더 결합할 게 없는 리스트 길이 2인 것들로 pi 구성
for i in columns:
    for j in i:
        if len(j) == 2:
            prime_implicants.append(j)
    if i != []:
        print(f"\n\n{col_num}번째 column :")
        for k in i:
            print(k)
        col_num += 1

# 중복 제거를 위해 정렬
for i in prime_implicants:
    i[0].sort()

# Prime_implicants 중 중복을 제거한다
temp = []
for i in prime_implicants:
    if i not in temp:
        temp.append(i)
prime_implicants = temp

# 차트를 그리기 위해 ''와 '*'을 순서에 맞게 삽입
for i in prime_implicants:
    i.append([])
    for k in range(0, len(minterm_expression_decimal_int)):
        i[2].append('')

    for k in range(0, len(minterm_expression_decimal_int)):
        for j in i[0]:
            if j == minterm_expression_decimal_int[k]:
                i[2][k] = '*'

# 테이블 출력용 판다스
print("\n\n------- 차트 -------")
temp = ['Prime Implicants'] + ['binary'] + minterm_expression_decimal_int
df = pd.DataFrame(temp)
df = df.transpose()
for i in prime_implicants:
    temp = []
    temp.append(",".join(list(map(str, i[0]))))
    temp = temp + [i[1]] + i[2]
    df.loc[len(df)] = temp
print(df)

# minterm 별 pi들의 개수
minterm_count = []
for i in range(0, len(minterm_expression_decimal_int)):
    minterm_count.append(0)

for i in prime_implicants:
    for j in range(0,len(i[2])):
        if i[2][j] == '*':
            minterm_count[j] += 1

# minterm count가 1인것을 이용해 essential pi를 구함
essential_prime_implicants = []
for i in range(0, len(minterm_count)):
    if minterm_count[i] == 1:
        for j in prime_implicants:
            if j[2][i] == '*':
                if len(j) < 4:
                    essential_prime_implicants.append(j)
                    j.append('v')

print("\nEssential Prime Implicants : ")
for i in essential_prime_implicants:
    print(i[0])
print("\n")

# essential pi를 적용한 후 남은 minterm_count 완료값 = -1
for i in essential_prime_implicants:
    for j in range(0,len(i[2])):
        if i[2][j] == '*':
            minterm_count[j] = -1

while 1 :
    # 모든 민텀이 지워지면 탈출
    break_judge = 0
    for i in minterm_count:
        if i != -1:
            break_judge = 1
    if break_judge == 0:
        break

    # 남은 pi 중 남은 minterm을 가장 많이 만족하는 pi 를 찾기 위해
    # pi count 0으로 초기화
    pi_count = []
    for i in range(0, len(prime_implicants)):
        pi_count.append(0)

    # 해결되지 않은 minterm을 포함하고 있는 개수만큼 pi_count 리스트에 추가
    for i in range(0, len(minterm_count)):
        if minterm_count[i] != -1:
            for j in range(0, len(prime_implicants)):
                if prime_implicants[j][2][i] == '*':
                    pi_count[j] += 1

    # pi_list의 값이 가장 큰 pi = 가장 많은 minterm을 지울 수 있는 pi
    # 모든 minterm이 지워질 때 까지 가장 많은 minterm을 지울 수 있는 pi를 인덱스로 찾아 저장
    next_pi = prime_implicants[pi_count.index(max(pi_count))]
    prime_implicants[pi_count.index(max(pi_count))].append("v")
    for i in range(0, len(next_pi[2])):
        if next_pi[2][i] == "*":
            minterm_count[i] = -1



# 사용한 pi는 v를 추가하여 list의 길이가 4이므로 4인 리스트들 모아서 결과로 저장하고 출력
print("사용한 모든 Prime Implicants : ")
result_binarys = []
for i in prime_implicants:
    if len(i) == 4:
        result_binarys.append(i[1])
        print(i[0])

result_abcs = []
for i in result_binarys:
    result_abcs.append(binary_to_abc(i))

THE_RESULT = " + ".join(result_abcs)
print(f"\n따라서 답은 : {THE_RESULT}")