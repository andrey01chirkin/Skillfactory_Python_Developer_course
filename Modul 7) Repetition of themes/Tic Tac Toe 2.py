def print_board(board) -> None:
    """
    Функция, которая будет отображать текущее состояние игрового поля в консоли.
    :param board:
    :return: None
    """
    print(' ', 0, 1, 2)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0:
                print(i, end=' ')
            print(board[i][j], end=' ')
        print()


def check_completion_game(board, number_player: int, mark: str) -> bool:
    """
    Проверка на завершенность игры. Функция вернет True в случае победы и в случае ничьи.
    :param board:
    :param number_player:
    :param mark:
    :return: bool
    """
    if any([  # Условия победы
        [3*mark] in board,  # Проверка равенства значений в строке
        set([board[index_row][0] for index_row in range(3)]) == set(mark),  # Проверка равенства в столбце с индексом 0
        set([board[index_row][1] for index_row in range(3)]) == set(mark),  # Проверка равенства в столбце с индексом 1
        set([board[index_row][2] for index_row in range(3)]) == set(mark),  # Проверка равенства в столбце с индексом 2
        board[0][0] == board[1][1] == board[2][2] == mark,  # Проверка равенства значений по диагонале
        board[0][2] == board[1][1] == board[2][0] == mark  # Проверка равенства значений по диагонале
    ]):
        print(f"Игрок {number_player} победил!")
        return True
    else:
        max_amount_items = 9
        if sum(row.count('X') + row.count('0') for row in board) == max_amount_items:
            print("Ничья")
            return True
        return False


def input_data_player(board, number_player, mark):
    while True:  # Игрок вводит данные пока не пройдут проверку
        print(f"\nИгрок {number_player} ваш ход")
        row_index = input("Введите индекс строки: ")
        if row_index in ('0', '1', '2'):
            row_index = int(row_index)
            col_index = input("Введите индекс столбца: ")
            if col_index in ('0', '1', '2'):
                col_index = int(col_index)
                if board[row_index][col_index] not in ('X', '0'):
                    board[row_index][col_index] = mark
                    if check_completion_game(board, number_player, mark):  # Проверка на завершенность игры
                        print_board(board)
                        return True
                    print_board(board)
                    return False
                else:
                    print("Ячейка занята!")
                    print_board(board)
                    continue
            else:
                print("Индекс столбца должен быть числом от 0 до 2!")
                print_board(board)
                continue
        else:
            print("Индекс строки должен быть число от 0 до 2!")
            print_board(board)
            continue


def input_data():
    print("-----Добро пожаловать в игру крестики нолики-----")
    board: list[list[str]] = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    print_board(board)
    while True:
        if input_data_player(board, 1, 'X') or input_data_player(board, 2, '0'):
            break


input_data()
