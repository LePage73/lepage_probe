# Дополнительное практическое задание по модулю 3
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def any_counter(*data_structure, len_=0):
  #print('зашло в функцию ',str(data_structure))
  for struct_ in data_structure:
    #print('разбирается по элементно в цикле', struct_)
    if isinstance(struct_,int):
      len_ += int(struct_)
      #print('тип число', struct_,' длина ', len_)
      continue
    elif isinstance(struct_,str):
      len_ += len(struct_)
      #print('тип строка ', struct_,' длина ', len_)
      continue
    elif isinstance(struct_, list):
     # print('тип список ', struct_)
      len_ = any_counter(*struct_,len_ = len_)
      continue
    elif isinstance(struct_, dict):
      #print('тип словарь, разбиваем пары в цикле ', struct_)
      for item in struct_.items():
          len_ = any_counter(item,len_ = len_)
          continue
    elif isinstance(struct_,tuple):
     #print('тип кортеж ', struct_)
      for element_ in struct_:
          len_ = any_counter(element_, len_ = len_)
          continue
    elif isinstance(struct_, set):
        #print('тип множество ', struct_)
        len_ = any_counter(*struct_, len_=len_)
    else:
      #print('если сюда зашли то непонятки')
      return len_
  #print('exit len = ', len_)
  return len_

print(data_structure)
print('result ', any_counter(data_structure))
## P.S. Хотя проще было превратить data_structure в строку, повыбрасывать все лишние символы и разобрать в цикле