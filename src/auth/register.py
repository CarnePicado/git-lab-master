def register_user(username: str, password: str, users: dict[str, str]) -> bool:
    """Регистрирует пользователя; возвращает False, если логин уже занят."""
    if username in users:
        return False
    if not username or not password:
        return False
    users[username] = password
    return True
