import doctest


class PackOfCigarets:
    def __init__(self, name: str, price: int, amount_sig: int):
        """
        Создание объекта пачка сигарет (курение вредит вашему здоровью)
        :param name: Название сигарет
        :param price: Цена
        :param amount_sig: Оставшееся количество сигарет в пачке

        Пример:
        >>> pack_of_sigs = PackOfCigarets('Camel', 190, 20) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError('Название должно быть типа str')
        if not name:
            raise ValueError('Название не может быть меньше 1 символа')
        self.name = name

        if not isinstance(price, int):
            raise TypeError('цена должна быть типа int')
        if price < 0:
            raise ValueError('Цена сигарет может быть только положительной')
        self.price = price

        if not isinstance(amount_sig, int):
            raise TypeError('Количество сигарет должно быть типа int')
        if not (0 < amount_sig <= 20):
            raise ValueError('Сигарет в пачке не может быть меньше 1 или больше 20')
        self.amount_sig = amount_sig

    def smoke(self):
        """
        Метод выкуривания сигареты, ничего не возвращает,
        но меняет оставшееся количесво сигарет в пачке,
        если их 0 (пачка проверяется на наличие сигарет
        посредством метода is_empty_pack)
        то выдает предупреждение с текстом что нужно купить новую пачку сигарет.
        :return:

        Пример:
        >>> pack_of_sigs = PackOfCigarets('Camel', 190, 20)
        >>> pack_of_sigs.smoke()
        """
        ...

    def give_sig(self):
        """
        Метод который описывает акт передачи сигареты просящему(пачка также проверяется на наличие сигарет
        посредством метода is_empty_pack)
        :return: ничего не возвращает
        """
        ...

    def is_empty_pack(self) -> bool:
        """
        Метод проверки закончились ли сигареты в пачке
        :return: Является пачка пустой или нет

        Пример:
        >>> pack_of_sigs = PackOfCigarets('Camel', 190, 20)
        >>> pack_of_sigs.is_empty_pack()
        """
        ...


class Cat:
    def __init__(self, name: str, age: int, weight: int):
        """
        Создание объекта Кошка
        :param name: Имя кошки
        :param age: Возраст кошки
        :param weight: вес кошки

        Пример:
        >>> new_cat = Cat("Анфиса", 3, 3)
        """
        if not isinstance(name, str):
            raise TypeError('Имя должно быть типа str')
        if not name:
            raise ValueError('Имя не может быть меньше 1 символа')
        self.name = name

        if not isinstance(age, int):
            raise TypeError('Возраст кошки должен быть типа int')
        if age < 0:
            raise ValueError('Возраст может быть только положительным')
        self.age = age

        if not isinstance(weight, int):
            raise TypeError('Вес кошки должен быть типа int')
        if weight < 0:
            raise ValueError('Вес должен быть положительным')
        self.weight = weight

    def pet_cat(self):
        """
        Метод который дает возможность поласкать и погладить Кошку

        :return: Ничего не возвращает

        Пример:
        >>> new_cat = Cat("Анфиса", 3, 3)
        >>> new_cat.pet_cat()
        """
        ...

    def feed_cat(self):
        """
        Метод позволяющий покормить Кошку, который использует метод
        определения веса корма
        :return: Ничего не возвращает

        Пример:
        >>> new_cat = Cat("Анфиса", 3, 3)
        >>> new_cat.feed_cat()
        """
        ...

    def weight_of_food(self):
        """
        Метод позволяющий расчитать норму корма исходя из веса кошки

        :return: Возвращает вес корма

        Пример:
        >>> new_cat = Cat("Анфиса", 3, 3)
        >>> new_cat.weight_of_food()
        """
        ...


class Dog:
    def __init__(self, name: str, age: int):
        """
        Создание объекта Собака

        :param name: имя собаки
        :param age: возраст собаки

        Пример:
        >>> new_dog = Dog("Акира", 4)
        """
        if not isinstance(name, str):
            raise TypeError('Имя должно быть типа str')
        if not name:
            raise ValueError('Имя не может быть меньше 1 символа')
        self.name = name

        if not isinstance(age, int):
            raise TypeError('Возраст собаки должен быть типа int')
        if age < 0:
            raise ValueError('Возраст может быть только положительным')
        self.age = age

    def give_bone(self):
        """
        метод позволяющий дать собаке косточку
        :return: ничего не возвращает

        Пример:
        >>> new_dog = Dog("Акира", 4)
        >>> new_dog.give_bone()
        """
        ...

    def spin_tail(self):
        """
        Метод виляния хвостом)
        :return: ничего не возвращает

        Пример:
        >>> new_dog = Dog("Акира", 4)
        >>> new_dog.spin_tail()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
