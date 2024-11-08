def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    index_string = 1
    for text_line in strings:
        strings_position[index_string, file.tell()] = text_line
        file.write(text_line + '\n')
        index_string += 1
    file.close()
    return strings_position



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)