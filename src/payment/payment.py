def calculate_total(amount: float, fee_percent: float = 0.0) -> float:
    """Возвращает сумму платежа с комиссией."""
    return round(amount + amount * fee_percent / 100, 2)
