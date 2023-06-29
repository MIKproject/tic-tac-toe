class TicTacToe:
    cnt = 0

    def __init__(self):
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.flag = True

    def mark(self, i, j):
        if self.cnt == 0:
            if self.matrix[i-1][j-1] == ' ':
                if self.flag:
                    self.matrix[i-1][j-1] = 'X'
                    self.flag = False
                    if self.winner is None:
                        pass
                    else:
                        self.winner()
                else:
                    self.matrix[i-1][j-1] = 'O'
                    self.flag = True
                    if self.winner is None:
                        pass
                    else:
                        self.winner()
            else:
                return 'Недоступная клетка'
        else:
            return 'Игра окончена'

    def winner(self):
        for line in self.matrix:
            if ''.join(line) == 'XXX':
                return 'X'
            if ''.join(line) == 'OOO':
                return 'O'

        for line in zip(*self.matrix):
            if ''.join(line) == 'XXX':
                return 'X'
            if ''.join(line) == 'OOO':
                return 'O'

        s1 = s2 = ''
        for i in range(3):
            s1 += self.matrix[i][i]
            s2 += self.matrix[i][~i]
        if s1 == 'XXX' or s2 == 'XXX':
            return 'X'
        if s1 == 'OOO' or s2 == 'OOO':
            return 'O'

        if ' ' not in sum(self.matrix, []):
            return 'Ничья'

    def show(self):
        for i in range(len(self.matrix)):
            row = ''
            for j in range(len(self.matrix)):
                row += self.matrix[i][j] + '|'
            print(row.rstrip('|'))
            if i != 2:
                print('-----')


tictactoe = TicTacToe()

while tictactoe.winner() not in ['X', 'O', 'Ничья']:
    try:
        a, b = map(int, input('Введите координаты Х (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
    except Exception:
        print('Внимательно вводи координаты')
        a, b = map(int, input('Введите координаты Х (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
    if tictactoe.mark(a, b) == 'Недоступная клетка':
        s = tictactoe.mark(a, b)
        while s == 'Недоступная клетка':
            try:
                a, b = map(int, input('Введите координаты Х (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
            except Exception:
                print('Внимательно вводи координаты')
                a, b = map(int, input('Введите координаты Х (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
            s = tictactoe.mark(a, b)
    tictactoe.mark(a, b)
    tictactoe.show()
    if tictactoe.winner() in ['X', 'O', 'Ничья']:
        break

    try:
        x, y = map(int, input(
            'Введите координаты O (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
    except Exception:
        print('Внимательно вводи координаты')
        x, y = map(int, input(
            'Введите координаты O (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
    if tictactoe.mark(x, y) == 'Недоступная клетка':
        s = tictactoe.mark(x, y)
        while s == 'Недоступная клетка':
            try:
                x, y = map(int, input(
                    'Введите координаты O (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
            except Exception:
                print('Внимательно вводи координаты')
                x, y = map(int, input(
                    'Введите координаты O (две цифры от 1 до 3 ЧЕРЕЗ ПРОБЕЛ, где первая цифра СТРОКА, вторая СТОЛБЕЦ): ').split())
            s = tictactoe.mark(x, y)
    tictactoe.mark(x, y)
    tictactoe.show()
    if tictactoe.winner() in ['X', 'O', 'Ничья']:
        break

print(f'Поздравляю {tictactoe.winner()} победил')