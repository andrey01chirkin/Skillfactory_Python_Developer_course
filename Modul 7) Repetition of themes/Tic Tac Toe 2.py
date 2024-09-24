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


def check_completion_game(board: list[list[str]], number_player: int, mark: str) -> bool:
    """
    Функция проверяет завершенность игры.
    :param board:
    :param number_player:
    :param mark:
    :return: Bool
    """
    if any([  # Условия победы
        [mark] * 3 in board,  # Проверка равенства значений в строке
        (mark,) * 3 in list(zip(*board)),  # Проверка равенства значений в столбце
        [mark] * 3 == [row[i] for i, row in enumerate(board)],  # Проверка равенства значений по диагонали
        [mark] * 3 == [row[i] for i, row in enumerate(board[::-1])]  # Проверка равенства значений по противоположной диагонали
    ]):
        print(f"Игрок {number_player} победил!")
        return True
    else:
        max_amount_items = 9
        if sum(row.count('X') + row.count('0') for row in board) == max_amount_items:
            print("Ничья")
            return True
        return False


def input_data_player(board: list[list[str]], number_player: int, mark: str) -> bool:
    """
    Функция обеспечивает ввод данных и проверку корректности ввода.
    :param board:
    :param number_player:
    :param mark:
    :return:
    """
    while True:
        print(f"\nИгрок {number_player} ваш ход")
        row_index = input("Введите индекс строки: ")
        if row_index in ('0', '1', '2'):
            row_index = int(row_index)
            col_index = input("Введите индекс столбца: ")
            if col_index in ('0', '1', '2'):
                col_index = int(col_index)
                if board[row_index][col_index] not in ('X', '0'):
                    board[row_index][col_index] = mark
                    print_board(board)
                    return check_completion_game(board, number_player, mark)  # Проверяет на завершенность игры
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
    while True:
        if input_data_player(board, 1, 'X') or input_data_player(board, 2, '0'):
            break


main()
