immutable_var = 1, 5, 'редиска', 'чай', True
print('Immutable var', immutable_var)
#Кортеж неизменен, это константа. Но изменения могу быть внутри одного из элементов, если позволяет его функционал. Например, в кортеже могут содержаться списки.
mutable_list = [1, 5, 'редиска', 'чай', True]
print('Mutable list', mutable_list)
mutable_list.append(152)
mutable_list[1] = 777
print('Modified mutable list', mutable_list)

