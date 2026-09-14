s = "hola"
i = 5
f = 2.5
b = True
l = [1,2,3]

result_str_str = s + s
#result_str_int = s + i ----- da error
#result_int_str = i + s ----- da error
result_bool_bool = b + b
result_bool_int = b + i
#result_bool_str = b + s ----- da error
result_list_list = l + l
#result_str_list = s + l ----- da error

print(result_str_str)
print(result_bool_bool)
print(result_bool_int)
print(result_list_list)

#

