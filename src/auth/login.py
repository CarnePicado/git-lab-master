def authenticate(username: str, password: str, users: dict[str, str]) -> bool:
    """Проверяет пару логин/пароль по учебному хранилищу пользователей."""
    return users.get(username) == password
