import ast

def input_int():
    while True:
        user_input = input()
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное целое число.")


def input_matrix(n):
    matrix = []
    print(f"Введите элементы матрицы размером {n}x{n}:")

    for i in range(n):
        while True:
            row_input = input(f"Строка {i + 1}: ")
            row_elements = row_input.split()

            if len(row_elements) != n:
                print(f"Ошибка: Введите ровно {n} элементов для строки {i + 1}.")
                continue

            try:
                row = [int(x) for x in row_elements]
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: Все элементы должны быть целыми числами.")

    return matrix

def chinese_zodiac():
    zodiac_years = [
        "Крыса", "Бык", "Тигр", "Кролик", "Дракон",
        "Змея", "Лошадь", "Коза", "Обезьяна", "Петух",
        "Собака", "Свинья"
    ]

    while True:
        year_input = input("Введите год (или 0 для выхода): ")
        if year_input == '0':
            break

        if not year_input.isdigit():
            print("Пожалуйста, введите корректный год.")
            continue

        year = int(year_input)
        zodiac_index = (year - 4) % 12  # 4 - это 2004 год, год Крысы
        print(f"Год {year} соответствует знаку: {zodiac_years[zodiac_index]}")



def process_input(data):
    try:
        print("Целое число")
        a = int(data)
        return sum(int(digit) for digit in str(data) if int(digit) % 2 != 0)
    except ValueError:
        pass

    if isinstance(data, str):
        if data.startswith('[') and data.endswith(']'):
            data = ast.literal_eval(data)
        elif data.startswith('(') and data.endswith(')'):
            data = ast.literal_eval(data)
    if isinstance(data, list):
        print("Список")
        filtered_list = [x for x in data if x >= 0]
        if 0 in filtered_list:
            zero_index = filtered_list.index(0)
            return sum(filtered_list[zero_index + 1:])
        return 0
    elif isinstance(data, tuple):
        print("Кортеж")
        max_elem = max(data)
        min_elem = min(data)
        new_tuple = tuple(min_elem if x == max_elem else max_elem if x == min_elem else x for x in data)
        return new_tuple
    elif isinstance(data, str):
        print("Строка")
        words = data.split()
        even_length_count = sum(1 for word in words if len(word) % 2 == 0)
        return even_length_count

    else:
        return "Неподдерживаемый тип данных."


def count_non_zero_columns(matrix):
    if not matrix:
        return 0

    num_columns = len(matrix[0])
    count = 0

    for col in range(num_columns):
        if all(matrix[row][col] != 0 for row in range(len(matrix))):
            count += 1

    return count


def try_except_finally_example():
    try:
        value = int(input("Введите число: "))
        print(f"Вы ввели: {value}")
    except ValueError:
        print("Ошибка: Введено не число.")
    finally:
        print("Это сообщение отображается всегда.")


def main():
    while(True):
        print("Меню:")
        print("1.Задача_1")
        print("2.Задача_2")
        print("3.Задача_3")
        print("4.Задача_4")
        print("0.Выход")
        print("Введите номер задания: ")
        inp = input_int()
        if inp == 1:
            chinese_zodiac()
        elif inp == 2:
            print("Совершите ввод(список, кортеж, число, строка)")
            print(process_input(input()))
        elif inp == 3:
            print(count_non_zero_columns(input_matrix(4)))
        elif inp == 4:
            try_except_finally_example()
        elif inp == 0:
            return;



if __name__ == "__main__":
    main()
