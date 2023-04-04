from dataclasses import dataclass


@dataclass
class BasicWord:
    original_word: str
    acceptable_words: list

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
