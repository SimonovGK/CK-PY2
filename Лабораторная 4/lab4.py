
class Movie:
    """
    Создание и подготовка к работе объекта "Кинематограф" (включает в себя фильмы, сериалы)
    :param name: Название
    :param duration: Продолжительность
    Примеры:
    >>> the_platform = Movie('The Platform', 1.34) # инициализация экемпляра класса
    """
    def __init__(self, name: str, duration: float):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"Кинопроизведение {self.name}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, duration={self.duration!r})"

    def get_genre(self) -> str:
        """
        Метод определющий жанр Кинопроизведения
        :return: Является ли мультфильм 2D или 3D
        Примеры:
        >>> the_platform = Movie('The Platform', 1.34) # инициализация экемпляра класса
        >>> the_platform.get_genre()
        """
        ...


class Series(Movie):
    """
    Создание и подготовка к работе объекта "Сериалы"
    :param name: Название Сериала
    :param duration: Продолжительность 1 серии
    :param amount_of_episodes: Количество серий
    Примеры:
    >>> new_series = Series('Sherlock', 43.37, 62) # инициализация экемпляра класса
    """
    def __init__(self, name: str, duration: float, amount_of_episodes: int):
        super().__init__(name, duration)
        self.amount_of_episodes = amount_of_episodes

    def __str__(self):
        return f"Сериал {self.name}. Продолжительность {self.duration} одной из {self.amount_of_episodes} серий"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, duration={self.duration!r}, ' \
               f'amount_of_episodes={self.amount_of_episodes!r})'

    @property
    def amount_of_episodes(self):
        return self._amount_of_episodes

    @amount_of_episodes.setter
    def amount_of_episodes(self, amount_of_episodes: int):
        """
        Количество эпизодов сериала
        :param amount_of_episodes: количество серий
        :raise TypeError: Если количество серий не является типом int, то вызываем ошибку
        :raise ValueError: Если количество серий отрицательное или равно 0, то вызываем ошибку
        Примеры:
        >>> new_series = Series('Sherlock', 43.37, 62,)
        """
        if not isinstance(amount_of_episodes, int):
            raise TypeError("Количество серий должно быть типа int")
        if amount_of_episodes <= 0:
            raise ValueError("Количество серий должно быть положительным числом")
        self._amount_of_episodes = amount_of_episodes
