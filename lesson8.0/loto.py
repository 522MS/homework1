import random


class LotoGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self.numbers = 90
        self.keg = random.sample(range(1, self.numbers + 1), self.numbers)

    def get_keg(self):
        return self.keg.pop()

    def start_game(self):
        for i in range(self.numbers):
            print(self._player, self._computer)
            number = self.get_keg()
            print(f'Новый боченок: {number} (осталось {len(self.keg)})')
            yes_no = input('Зачеркнуть цифру? (y/n) ')
            if yes_no == 'y':
                if not self._player.delete_number(number):
                    print('Игрок проиграл!')
                    break
            elif yes_no == 'n':
                if self._player.number_in_card(number):
                    print('Игрок проиграл!')
                    break
            elif yes_no != 'y':
                print('Нет такого варианта. Вы проиграли!')
                break
            if self._computer.number_in_card(number):
                self._computer.delete_number(number)


class LotoPlayer:
    def __init__(self, player_card):
        self.player_card = player_card
        self.card = [[], [], []]
        self.max_number = 90
        self.max_number_card = 15
        self.numbers_line = 0
        self._numbers = random.sample(range(1, self.max_number + 1), self.max_number_card)
        for line in self.card:
            for i in range(5):
                line.append(self._numbers.pop())

        for index, line in enumerate(self.card):
            self.card[index] = sorted(line)

    def number_in_card(self, number):
        for line in self.card:
            if number in line:
                return True
        return False

    def delete_number(self, number):
        for index, line in enumerate(self.card):
            for num_index, number_card in enumerate(line):
                if number == number_card:
                    self.card[index][num_index] = '-'
                    self.numbers_line += 1
                    if self.numbers_line >= self.max_number_card:
                        raise Exception(f'{self.player_card} победил')
                    return True
        return False

    def __str__(self):
        heading = f'-----Карточка {self.player_card}а-----'
        line_feed = '\n'
        for line in self.card:
            for field in line:
                line_feed += f'{field} '
            line_feed += '\n'
        return heading + line_feed


player = LotoPlayer('Игрок')
computer = LotoPlayer('Компьютер')
loto = LotoGame(player, computer)
loto.start_game()
