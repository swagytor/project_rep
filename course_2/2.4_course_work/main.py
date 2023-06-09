from player import Player
import utils

# объявляем константы: адрес JSON-BIN и стоп-слова
URL_TO_JSON_BIN = 'https://api.npoint.io/3d60dd466f48461fb6f8'
STOPWORDS = ('стоп', 'stop', 'АСТАНАВИТЕСЬ')

print('Привет!\n'
      'Давай сыграем в игру "Игра в слова"')

# делаем проверку на корректное имя игрока
user_name = utils.get_valid_name()

# объявляем объект player класса Player
player = Player(user_name)

print(f'Приятно познакомиться, {player.user_name}!\n'
      'Давай начнём игру!')

print()

# загружаем одно случайное слово из JSON-BIN
game = utils.load_random_word(URL_TO_JSON_BIN)
# вычисляем количество загаданных слов
words_left = game.acceptable_words_counter()
# находим самое короткое слово в списке загаданных слов
shortest_word = utils.get_shortest_length(game.acceptable_words)

print(f'Составьте {game.acceptable_words_counter()} слов из слова {game.original_word.upper()}\n'
      f'Слова не должны быть короче {len(shortest_word)} букв\n\n'
      f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
      f'Поехали, ваше первое слово?')

while game.acceptable_words != player.added_words:
    print(f'\nСлово {game.original_word.upper()}\n'
          f'Осталось отгадать: {words_left}')

    guessed_word = input('Введите слово: ').strip().lower()

    if guessed_word in STOPWORDS:
        break

    elif len(guessed_word) < len(shortest_word):
        print('\033[31m' + 'Слишком короткое слово!' + '\033[39m')

    elif not game.is_exist(guessed_word):
        print('\033[31m' + 'Данного слова нет списке загаданных!' + '\033[39m')

    elif player.is_added(guessed_word):
        print('\033[31m' + 'Данное слово уже было введено!' + '\033[39m')

    # в случае выполненных условий добавляем введённое слово в множество added_words
    else:
        print('Слово принято!')
        player.add_word(guessed_word)
        words_left -= 1

print()

print(f'{player.user_name}, игра завершена!\n'
      f'Вы угадали {player.added_words_counter()} слов!')
