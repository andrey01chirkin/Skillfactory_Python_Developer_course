def print_board(board: list[list[str]]) -> None:
    """
    Функция отображает текущее состояние игрового поля в консоли.
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


def check_completion_game(board: list[list[str]], mark: str) -> bool:
    """
    Функция проверяет завершенность игры.
    :param board:
    :param mark:
    :return: Bool
    """
    return any([  # Условия победы
        [mark] * 3 in board,  # Проверка равенства значений в строке
        (mark,) * 3 in list(zip(*board)),  # Проверка равенства значений в столбце
        [mark] * 3 == [row[i] for i, row in enumerate(board)],  # Проверка равенства значений по диагонали
        [mark] * 3 == [row[i] for i, row in enumerate(board[::-1])] # Проверка равенства значений по противоположной диагонали
    ]) or False


def input_data_player(board: list[list[str]], number_player: int, mark: str) -> bool:
    """
    Функция обеспечивает ввод данных и проверку корректности ввода.
    :param board:
    :param number_player:
    :param mark:
    :return: Bool
    """
    while True:
        print(f"\nИгрок {number_player} ваш ход")
        row_index = input("Введите индекс строки: ")
        if row_index not in ('0', '1', '2'):
            print("Индекс строки должен быть числом от 0 до 2!")
            print_board(board)
            continue

        col_index = input("Введите индекс столбца: ")
        if col_index not in ('0', '1', '2'):
            print("Индекс столбца должен быть число от 0 до 2!")
            print_board(board)
            continue

        row_index = int(row_index)
        col_index = int(col_index)

        if board[row_index][col_index] not in ('X', '0'):
            board[row_index][col_index] = mark
            print_board(board)
            return check_completion_game(board, mark)  # Проверяет на завершенность игры
        else:
            print("Ячейка занята!")
            print_board(board)


def main() -> None:
    """
    Функция обеспечивает окончание выполнения программы в случае победы или ничьи.
    :return: None
    """
    print("-----Добро пожаловать в игру крестики нолики-----")
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    print_board(board)

    max_amount_items = 9
    for i in range(max_amount_items):

        number_player = 1
        if input_data_player(board, number_player, 'X'):
            print(f"Игрок {number_player} победил!")
            break

        number_player = 2
        if input_data_player(board, number_player, '0'):
            print(f"Игрок {number_player} победил!")
            break

        if i == max_amount_items - 1:
            print(f"Ничья!")


main()
