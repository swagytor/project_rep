class Player:
    """
    Класс игрока
    """
    def __init__(self, user_name):
        self.user_name = user_name
        self.added_words = set()

    def __repr__(self):
        return f"Player{self.user_name, self.added_words}"

    def added_words_counter(self) -> int:
        """
        Возвращает количество угаданных слов
        """
        return len(self.added_words)

    def add_word(self, word: str) -> None:
        """
        Добавляет слово в список угаданных слов
        :param word: введённое пользователем слово
        """
        self.added_words.add(word)

    def is_added(self, word: str) -> bool:
        """
        Проверяет, было ли введеное слово уже использовано
        :param word: введённое пользователем слово
        :return: булевое значение
        """
        return word in self.added_words
