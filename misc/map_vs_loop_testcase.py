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

# Creating two iterators

list1 = [1, 2, 4, 5]
list2 = [5, 2, 8, 3]
# Using map with lambda to pass the two iterators
list1_list2 = map(lambda x1, x2: x1+x2, list1, list2)
# Observing the result
print(list(list1_list2))  # Output is [6, 4, 12, 8]

