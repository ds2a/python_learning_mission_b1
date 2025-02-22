
input_list = [1,5,3,7,4,6,2]
given_sum_value = 9

# result  [(5,4), (6,3),(7,2)]

result = []
result1 = []

for first_num in input_list:

    pair_number = given_sum_value - first_num
    if pair_number in input_list:
        result.append((first_num, pair_number))

print(result)


for first_num in input_list:
    pair_number = given_sum_value - first_num
    search_index_start_position = input_list.index(first_num)
    if pair_number in input_list[search_index_start_position:]:
        result1.append((first_num, pair_number))

print(result1)









