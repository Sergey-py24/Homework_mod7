
def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
            st_pos = file.tell()
            file.write(string + '\n')
            strings_positions[(len(strings_positions) + 1, st_pos)] = string
    file.close()
    return strings_positions



info = [ 'Text for tell.',
         'Используйте кодировку utf-8.',
         'Because there are 2 languages!',
         'Спасибо!']

result = custom_write('testing.txt', info)
for element in result.items():
    print(element)
