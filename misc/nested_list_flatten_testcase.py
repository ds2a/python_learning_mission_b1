input_list = [1,2,3,[4,5,[6,7]]]

result = []
def flatten(l):
    for e in l:

        # if isinstance(l, list):
        # if type(e) == list:
        if type(e) is list:
           flatten(e)
        else:
           result.append(e)


flatten(input_list)
print(result)



result1 = []
def flatten_with_out_recursion(l):
    for e in l:
        if type(e) is list:
          for e1 in e:
              if type(e1) == list:
                  result1.extend(e1)
              else:
                  result1.append(e1)
        else:
           result1.append(e)
flatten_with_out_recursion(input_list)
print(result1)



'''
1.recursion
2. multiple ways to check object type 
      # if isinstance(l, list):
      # if type(e) == list:
      if type(e) is list:
3.if sublist does not contain sub list we can simply wrote this program with out recursion approach ,
 just using list class method like append vs extend
 
'''

nested_list_without_sub_list =  [1,2,3,[4,5],[6,7]]
result2 = []
for e in nested_list_without_sub_list:
    if type(e) is list:
        result2.extend(e)
    else:
        result2.append(e)

print(result2)
