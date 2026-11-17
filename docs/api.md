# API проекта

## Авторизация

`authenticate(username, password, users) -> bool`

Проверяет, совпадает ли пароль с паролем пользователя в переданном словаре.

## Регистрация

`register_user(username, password, users) -> bool`

Добавляет пользователя в словарь. Возвращает `False`, если логин занят или переданы пустые значения.

## Оплата

`calculate_total(amount, fee_percent=0.0) -> float`

Рассчитывает сумму с учётом комиссии в процентах.
