# Дополнительное практическое задание по модулю: "Основные операторы"

def get_pair(m):
    list_pair = []
    for first_number in list(range(1,21)):
        for second_number in list(range(first_number + 1,21)):
            if m % (first_number+second_number) == 0:
                list_pair.append(first_number)
                list_pair.append(second_number)
    return list_pair

while True:
    m = int(input('введите первое число '))
    if m<3 or m>20:
        print('число должно быть от 3 до 20')
    else: break

pairs = get_pair(m)
text_pairs = str(pairs)
text_pairs = text_pairs.replace(', ','')
text_pairs = text_pairs.replace('[','')
text_pairs = text_pairs.replace(']','')

print('пары ', *pairs)
print('Пароль ', text_pairs)
