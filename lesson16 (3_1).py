# Домашняя работа по уроку "Пространство имён"
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(in_string):
    count_calls()
    return tuple([len(in_string),in_string.upper(), in_string.lower()])

def is_contains (in_string, in_list):
    count_calls()
    while len(in_list) > 0:
        if in_string.lower() == in_list.pop(0).lower(): return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('urBAN'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)