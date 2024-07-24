# изменяемые и не изменяемые объекты. Кортежи.


immutable_var = (1,2,3,4,'five')
print ('immutabe_var before change:', immutable_var)
#immutable_var[4] = 5
print ('immutabe_var after change:', immutable_var)

mutable_list =  [1,2,3,4,'five']
print ('mutabe_list before change:', mutable_list)
mutable_list[4] = 5
print ('mutable_list after change:', mutable_list)