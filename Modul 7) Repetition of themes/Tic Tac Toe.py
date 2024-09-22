
data: list[list[str]] = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board() -> None:
    """
    Функция, которая будет отображать текущее состояние игрового поля в консоли.
    :return: None
    """
    print(' ',0,1,2)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j == 0:
                print(i, end=' ')
            print(data[i][j], end=' ')
        print()

def check_completion_game(number_player: int, mark: str, counter_items: int) -> bool:
    """
    Проверка на завершенность игры. Функция вернет True в случае победы и в случае ничьи.
    :param number_player:
    :param mark:
    :param counter_items:
    :return: bool
    """
    if any([ #Условия победы
        [mark, mark, mark] in data, #Проверка равенства значений в строке
        set([data[index_row][0] for index_row in range(3)]) == set(mark), #Проверка равенства в столбце с индексом 0
        set([data[index_row][1] for index_row in range(3)]) == set(mark), #Проверка равенства в столбце с индексом 1
        set([data[index_row][2] for index_row in range(3)]) == set(mark), #Проверка равенства в столбце с индексом 2
        data[0][0] == data[1][1] == data[2][2] == mark, #Проверка равенства значений по диагонале
        data[0][2] == data[1][1] == data[2][0] == mark #Проверка равенства значений по диагонале
    ]):
        print(f"Игрок {number_player} победил!")
        return True
    else:
        max_amount_items = 9
        if counter_items == max_amount_items:
            print("Ничья")
            return True

        return False


def check_input(number_player: int) -> tuple[bool, int, int] | tuple[bool, int, None]:
    """
    Функция проверяет коррекность ввода индексов строки и столбца. Если индексы строки
    и столбца в диапозоне от 0 до 2 и по данным индексам еще не установлено значение О или Х, вернет True.
    В противном случае вернет False.
    :param number_player:
    :return: tuple[bool, int, int] | tuple[bool, int, None]
    """
    print(f"\nИгрок {number_player}")
    row_index: int = int(input("Введите индекс строки: "))
    if row_index in (0, 1, 2):
        col_index: int = int(input("Введите индекс столбца: "))
        if col_index in (0, 1, 2):
            if data[row_index][col_index] not in ('X', 'O'): #Проверка не ставит ли пользователь крестик или нолик повторно. Если X или O не были установлены по указанному индексу, возвращаем статус и индексы строки и столбца
                return True, row_index, col_index
            else:
                print("Ячейка занята")
                return False, row_index, col_index
        else:
            print("Индекс столбца должен быть в диапозоне от 0 до 2")
            return False, row_index, col_index
    else:
        print("Индекс строки должен быть в диапозоне от 0 до 2")
        return False, row_index, None

def input_data() -> None:
    """
    Функция осуществляет запись данных для двух игроков в двумерный массив Data если функция check_input вернет True.
    :return: None
    """
    global data
    counter_items: int = 0

    while True:
        amount_marks = sum([row.count('X') + row.count('O') for row in data])
        if amount_marks % 2 == 0: #Проверка на четное количество элементов необходима, если второй игрок ошибся с вводом индексов, он мог повторно ввести значения. При следующей итерации цикла ввод будет запрошен у второго пользователя, если кол-во элементов нечетное.
            mark: str = 'X'
            number_player: int = 1
            answer: bool
            row_index: int
            col_index: int
            answer, row_index, col_index = check_input(number_player) #Вернет (answer = True) если индекс строк и столбцов в диапозоне от 0 до 2 и ячейка указанная пользователем не заполнена Х или О
            if answer:
                data[row_index][col_index] = mark #Если ответ True происходит запись в двумерный массив
                counter_items += 1 #Подсчет кол-ва вставленных элементов (X и O)
                if check_completion_game(number_player, mark, counter_items): #Проверка на завершенность игры
                    print_board()
                    break
                print_board()
            else:
                print_board()
                continue
        else:
            mark: str = 'O'
            number_player: int = 2
            answer: bool
            row_index: int
            col_index: int
            answer, row_index, col_index = check_input(number_player) #Вернет (answer = True) если индекс строк и столбцов в диапозоне от 0 до 2 и ячейка указанная пользователем не заполнена Х или О
            if answer:
                data[row_index][col_index] = mark #Если ответ True происходит запись в двумерный массив
                counter_items += 1 #Подсчет кол-ва вставленных элементов (X и O)
                if check_completion_game(number_player, mark, counter_items): #Проверка на завершенность игры
                    print_board()
                    break
                print_board()
            else:
                print_board()
                continue

print_board()
input_data()