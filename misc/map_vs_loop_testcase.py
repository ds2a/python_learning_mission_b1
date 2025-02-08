#sqaure the items present in list

input_list = [2,10,5,6]

#approach 1 : Using for loop
result_list = []
for e in input_list:
    result_list.append(e*e)
print(result_list)


#approach 2 : Using list comprehension
result_list_1 = [e*e for e in input_list]
print(result_list_1)

#approach 3: Using map function approach
result_list_2 = list(map(lambda e:e*e, input_list))
print(result_list_2)

