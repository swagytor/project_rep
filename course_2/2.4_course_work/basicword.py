class BasicWord:
    """
    Класс основного слова
    """
    def __init__(self, original_word, acceptable_words):
        self.original_word = original_word
        self.acceptable_words = acceptable_words

    def __repr__(self):
        return f"BasicWord{self.original_word.title(), self.acceptable_words}"

    def is_exist(self, word: str) -> bool:
        """
        Есть ли введённое слово в загаданных
        :param word: Введённое слово
        :return: Булевое значение
        """
        return word in self.acceptable_words

    def acceptable_words_counter(self) -> int:
        """
        Возращает количество загаданных слов
        :return: Количество загаданных слов
        """
        return len(self.acceptable_words)
