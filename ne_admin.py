class User:
    def __init__(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            username: str | None = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(cls, first_name, last_name):
        user = cls(first_name=first_name, last_name=last_name)
        return user

    # Опишите метод класса with_username.
    @staticmethod
    def is_username_allowed(username):
        if username.startswith('admin'):
            return False
        return True

    @classmethod
    def with_username(cls, username):
        if not cls.is_username_allowed(username):
            raise ValueError("Некорректное имя пользователя")
        user = cls(username=username)
        return user

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return f"{self.username}"
        else:
            return "Unknown"

stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
#ne_stas = User.with_username('admin_nestas_anonymous')
