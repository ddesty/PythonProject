def get_mask_card_number(card_number: int) -> str:
    """
    Принимает номер карты (int) и возвращает его маску в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты (целое число)
    :return: Маска номера карты в строковом формате
    """
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Принимает номер счета (int) и возвращает его маску в формате **XXXX.

    :param account_number: Номер счета (целое число)
    :return: Маска номера счета в строковом формате
    """
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
