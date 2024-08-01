def first_word(text):
    # замінюємо всі крапки та коми на пробіли
    cleaned_text = text.replace('.', ' ').replace(',', ' ')
    # видаляємо пробіли з початкку рядка
    cleaned_text = cleaned_text.lstrip()
    # розбиваємо рядок на слова повертаємо перше слово
    words = cleaned_text.split()
    # перше слово або пустий рядок якщо немає слів
    return words[0] if len(words) > 0 else ''


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
