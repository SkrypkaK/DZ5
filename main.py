# №1 Сконвертуйте лист градусів у Цельсіях до Фаренгейтів. (Лист [0, 10, 20, 30, 40]). Формула для обчислення: (c * 9/5) + 32
# def square(c):
#     return (c*9/5)+32
# numbers = [10,20,30,40]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)

# №2 Порахуйте довжину кожної строки (Лист ['apple', 'banana', 'orange', 'kiwi'])
# def lang(c):
#     return len (c)
# numbers = ['appel', 'banana', 'orange','kivi']
# squared_numbers = map(lang,numbers)
# print(list(squared_numbers))

# №3 Сконвертуйте лист строк у верхній регістр (Лист ['hello', 'world', 'python', 'programming'])
# letters = ['hello', 'world', 'python', 'programming']
# for i in range(len(letters)):
#     letters[i] = letters[i].upper()
# letters = [x.upper() for x in letters]
# print(letters)

# №4 Відфельтруйте слова, довжина яких менша за 5 (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape'])
# letters = ['apple', 'banana', 'orange', 'kiwi', 'grape']
# filtered_letters = list(filter(lambda x: len(x) >= 5, letters))
# print(filtered_letters)

# №5 Відфельтруйте пусті строки (Лист ['hello', '', 'world', 'python', '', 'programming'])
# letters = ['hello', '', 'world', 'python', '', 'programming']
# filtered_letters = list(filter(lambda x: x != '', letters))
# print(filtered_letters)

# №6 Відфельтруйте слова, що НЕ починаються з літери ‘a’ (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado'])
# letters = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado']
# filtered_letters = list(filter(lambda x: x[0] == 'a', letters))
# print(filtered_letters)

# №7 Порахуйте сумму елементів (Лист [1, 2, 3, 4, 5])
# sheet = [1, 2, 3, 4, 5]
# sum_sheet = sum(sheet)
# print(sum_sheet)

# №8 Знайдіть найбільший елемент (Лист [23, 12, 56, 34, 78, 9, 67])
# sheet = [23, 12, 56, 34, 78, 9, 67]
# largest_element = max(sheet)
# print(largest_element)

# №9 Зробіть одну строку (з пробілами) з листу строк (Лист ['hello', 'world', 'python', 'programming'])
# lines = ['hello', 'world', 'python', 'programming']
# one_line = ' '.join(lines)
# print(one_line)



