from . import logger


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        Маскированный номер карты

    Raises:
        ValueError: Если номер карты невалидный
    """
    try:
        card_number_str = str(card_number)

        if len(card_number_str) != 16:
            error_msg = f"Номер карты должен содержать 16 цифр, получено {len(card_number_str)}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.debug(f"Замаскирован номер карты: {masked}")
        return masked

    except Exception as e:
        logger.error(f"Ошибка маскировки номера карты: {str(e)}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта в формате **XXXX.

    Args:
        account_number: Номер счёта

    Returns:
        Маскированный номер счёта

    Raises:
        ValueError: Если номер счёта слишком короткий
    """
    try:
        account_number_str = str(account_number)

        if len(account_number_str) < 4:
            error_msg = f"Номер счёта должен содержать минимум 4 цифры, получено {len(account_number_str)}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked = f"**{account_number_str[-4:]}"
        logger.debug(f"Замаскирован номер счёта: {masked}")
        return masked

    except Exception as e:
        logger.error(f"Ошибка маскировки номера счёта: {str(e)}")
        raise
